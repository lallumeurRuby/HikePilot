import { apiClient } from './client'
import type { RecommendationData } from '@/lib/types'

export async function requestRouteRecommendation(): Promise<RecommendationData> {
  return apiClient<RecommendationData>('/recommendations', { method: 'POST' })
}
