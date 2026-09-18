import { apiClient } from './client'
import type { SubmitQuestionnaireRequest } from '@/lib/types'

export async function submitQuestionnaireAnswers(payload: SubmitQuestionnaireRequest): Promise<void> {
  await apiClient<undefined>('/profile/questionnaire', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}
