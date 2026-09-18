'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { loginWithGoogle, ApiClientError } from '@/lib/api'
import { Toast } from '@/components/Toast'

// Google OAuth 本身不在本系統可測試邊界內（見 auth/使用者透過Google登入.feature 前置規則）
// 此頁面以可編輯欄位模擬 Google 帳號回傳的 profile 資訊
export default function LoginPage() {
  const router = useRouter()
  const [googleId, setGoogleId] = useState('g-001')
  const [email, setEmail] = useState('alice@example.com')
  const [name, setName] = useState('Alice')
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault()
    setSubmitting(true)
    setError(null)
    try {
      const data = await loginWithGoogle({ google_id: googleId, email, name })
      document.cookie = `auth-token=${data.token}; path=/`
      // Activity Diagram: S1 -> S2 一律導向問卷頁（可選擇是否更新既有答案）
      router.push('/questionnaire')
    } catch (err) {
      setError(err instanceof ApiClientError ? err.message : '登入失敗，請重試')
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <main style={{ maxWidth: 400, margin: '4rem auto', padding: '1rem' }}>
      <h1>HikePilot 登山路線推薦</h1>
      <p>使用 Google 帳號登入/註冊</p>
      <form onSubmit={handleLogin} data-testid="login-form">
        <label>
          Google ID
          <input
            data-testid="login-google-id"
            value={googleId}
            onChange={(e) => setGoogleId(e.target.value)}
            required
          />
        </label>
        <label>
          Email
          <input
            data-testid="login-email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label>
          姓名
          <input
            data-testid="login-name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <button data-testid="login-submit" type="submit" disabled={submitting}>
          {submitting ? '登入中…' : '使用 Google 帳號登入'}
        </button>
      </form>
      {error && <Toast message={error} onClose={() => setError(null)} />}
    </main>
  )
}
