import { http, HttpResponse } from 'msw'
import type { GeneratePlanRequest, GeneratePlanResponse, ErrorResponse } from '@/lib/types'
import { mockPlanSections, mockPdfUrl } from '../fixtures'
import { extractGoogleIdFromAuthHeader, getLastRecommendation } from '../state'

const API_BASE = '/api'

export const planHandlers = [
  http.post(`${API_BASE}/plans`, async ({ request }) => {
    const googleId = extractGoogleIdFromAuthHeader(request.headers.get('authorization'))
    const body = (await request.json()) as GeneratePlanRequest

    if (body.route_id === undefined || body.route_id === null) {
      const error: ErrorResponse = { success: false, error: { violation_type: 'ROUTE_NOT_SELECTED' } }
      return HttpResponse.json(error, { status: 400 })
    }

    const recommendedRoutes = googleId ? getLastRecommendation(googleId) : []
    const isInRecommendation = recommendedRoutes.some((r) => r.route_id === body.route_id)
    if (!isInRecommendation) {
      const error: ErrorResponse = { success: false, error: { violation_type: 'ROUTE_NOT_IN_RECOMMENDATION' } }
      return HttpResponse.json(error, { status: 422 })
    }

    const response: GeneratePlanResponse = {
      success: true,
      data: { sections: mockPlanSections, pdf_url: mockPdfUrl },
    }
    return HttpResponse.json(response, { status: 200 })
  }),
]
