import { setupWorker } from 'msw/browser'
import { http, HttpResponse, type JsonBodyType } from 'msw'
import { handlers } from './handlers'

const worker = setupWorker(...handlers)

function getHttpMethod(method: string) {
  switch (method) {
    case 'GET': return http.get
    case 'POST': return http.post
    case 'PUT': return http.put
    case 'DELETE': return http.delete
    default: return http.all
  }
}

// React 18 StrictMode（dev）會將 effect 呼叫兩次；worker.start() 不是「重複呼叫安全」的——
// 併發呼叫會讓第二次呼叫進入不一致狀態並可能靜默失敗，導致攔截失效。用模組層級的
// cached promise 確保 SW 只真正啟動一次，重複呼叫直接重用同一個 in-flight/已完成的 promise。
let startPromise: Promise<void> | null = null

export async function initMocks() {
  if (!startPromise) {
    startPromise = (async () => {
      await worker.start({ onUnhandledRequest: 'bypass' })

      // worker.start() 可能在 SW 已存在（非首次安裝）時提早 resolve，
      // 此時 navigator.serviceWorker.controller 尚未指向新一次導覽的文件，
      // 導致載入後立即發出的 fetch（如頁面 mount 時的請求）繞過攔截、打到真實網路。
      // 顯式等待 controller 就緒，確保 ready 狀態真正代表「請求會被攔截」。
      if (typeof navigator !== 'undefined' && navigator.serviceWorker && !navigator.serviceWorker.controller) {
        await new Promise<void>((resolve) => {
          const timeout = setTimeout(resolve, 2000)
          navigator.serviceWorker.addEventListener(
            'controllerchange',
            () => {
              clearTimeout(timeout)
              resolve()
            },
            { once: true }
          )
        })
      }
    })()
  }
  await startPromise

  // 測試模式：讀取 Playwright addInitScript 注入的 override
  const overrides = (window as any).__mswOverrides as Array<{
    method: string
    url: string
    body: unknown
    status: number
    delayMs?: number
  }> | undefined

  if (overrides?.length) {
    worker.use(
      ...overrides.map((o) =>
        getHttpMethod(o.method)(o.url, async () => {
          if (o.delayMs) await new Promise((r) => setTimeout(r, o.delayMs))
          return HttpResponse.json(o.body as JsonBodyType, { status: o.status })
        })
      )
    )
  }
}

export { worker }
