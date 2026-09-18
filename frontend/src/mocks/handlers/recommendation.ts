import { http, HttpResponse } from 'msw'
import type { RecommendationResponse, ErrorResponse } from '@/lib/types'
import { mockRoutes } from '../fixtures'
import { extractGoogleIdFromAuthHeader, getUser, getRequiredAnswered, setLastRecommendation } from '../state'

const API_BASE = '/api'

export const recommendationHandlers = [
  http.post(`${API_BASE}/recommendations`, ({ request }) => {
    const googleId = extractGoogleIdFromAuthHeader(request.headers.get('authorization'))
    if (!googleId || !getUser(googleId)) {
      const error: ErrorResponse = { success: false, error: { violation_type: 'UNAUTHENTICATED' } }
      return HttpResponse.json(error, { status: 401 })
    }

    if (!getRequiredAnswered(googleId)) {
      const error: ErrorResponse = { success: false, error: { violation_type: 'PROFILE_INCOMPLETE' } }
      return HttpResponse.json(error, { status: 422 })
    }

    const routes = mockRoutes.slice(0, 3)
    setLastRecommendation(googleId, routes)

    const response: RecommendationResponse = {
      success: true,
      data: { has_matches: routes.length > 0, routes },
    }
    return HttpResponse.json(response, { status: 200 })
  }),
]
