'use client'

import { useEffect, useState } from 'react'
import { useSearchParams } from 'next/navigation'
import { generateHikingPlan, ApiClientError } from '@/lib/api'
import type { GeneratePlanData } from '@/lib/types'
import { Toast } from '@/components/Toast'

export default function PlanPage() {
  const searchParams = useSearchParams()
  const routeId = searchParams.get('route_id')
  const [plan, setPlan] = useState<GeneratePlanData | null>(null)
  const [loading, setLoading] = useState(true)
  const [toast, setToast] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    async function load() {
      setLoading(true)
      try {
        const data = await generateHikingPlan({
          route_id: routeId ? Number(routeId) : undefined,
        })
        if (!cancelled) setPlan(data)
      } catch (err) {
        if (!cancelled) {
          setToast(err instanceof ApiClientError ? err.message || err.violationType : '規劃書生成失敗，請重試')
        }
      } finally {
        if (!cancelled) setLoading(false)
      }
    }
    load()
    return () => {
      cancelled = true
    }
  }, [routeId])

  if (loading) return <p>規劃書生成中…</p>

  return (
    <div style={{ maxWidth: 600 }}>
      <h1>登山規劃書</h1>
      {plan && (
        <div data-testid="plan-content">
          <ol>
            {plan.sections
              .slice()
              .sort((a, b) => a.section_order - b.section_order)
              .map((section) => (
                <li key={section.section_order} data-testid={`plan-section-${section.section_order}`}>
                  {section.section_name}
                </li>
              ))}
          </ol>
          <a data-testid="plan-pdf-link" href={plan.pdf_url} target="_blank" rel="noreferrer">
            下載 PDF
          </a>
        </div>
      )}
      {toast && <Toast message={toast} onClose={() => setToast(null)} />}
    </div>
  )
}
