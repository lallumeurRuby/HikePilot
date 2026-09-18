'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { requestRouteRecommendation, ApiClientError } from '@/lib/api'
import type { RouteSummary } from '@/lib/types'
import { Toast } from '@/components/Toast'

export default function RecommendationsPage() {
  const router = useRouter()
  const [loading, setLoading] = useState(false)
  const [hasRequested, setHasRequested] = useState(false)
  const [hasMatches, setHasMatches] = useState(false)
  const [routes, setRoutes] = useState<RouteSummary[]>([])
  const [toast, setToast] = useState<string | null>(null)

  async function handleRequestRecommendation() {
    setLoading(true)
    try {
      const data = await requestRouteRecommendation()
      setHasRequested(true)
      setHasMatches(data.has_matches)
      setRoutes(data.routes)
    } catch (err) {
      setToast(err instanceof ApiClientError ? err.message || err.violationType : '推薦失敗，請重試')
    } finally {
      setLoading(false)
    }
  }

  function handleSelectRoute(routeId: number) {
    router.push(`/plan?route_id=${routeId}`)
  }

  return (
    <div style={{ maxWidth: 600 }}>
      <h1>路線推薦</h1>
      <button data-testid="request-recommendation" onClick={handleRequestRecommendation} disabled={loading}>
        {loading ? '推薦中…' : hasRequested ? '重新推薦' : '請求路線推薦'}
      </button>

      {hasRequested && hasMatches && (
        <ul data-testid="recommendation-list" style={{ marginTop: '1rem' }}>
          {routes.map((route) => (
            <li key={route.route_id} style={{ marginBottom: '0.5rem' }}>
              {route.name}
              <button
                data-testid={`select-route-${route.route_id}`}
                onClick={() => handleSelectRoute(route.route_id)}
                style={{ marginLeft: '0.5rem' }}
              >
                選定此路線，生成規劃書
              </button>
            </li>
          ))}
        </ul>
      )}

      {hasRequested && !hasMatches && (
        <div data-testid="no-match-message" style={{ marginTop: '1rem' }}>
          <p>無符合資料</p>
          <a href="/questionnaire" data-testid="update-questionnaire-link">
            更新問卷後重新推薦
          </a>
        </div>
      )}

      {toast && <Toast message={toast} onClose={() => setToast(null)} />}
    </div>
  )
}
