import { apiClient } from './client'
import type { GeneratePlanRequest, GeneratePlanData } from '@/lib/types'

export async function generateHikingPlan(payload: GeneratePlanRequest): Promise<GeneratePlanData> {
  return apiClient<GeneratePlanData>('/plans', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}
