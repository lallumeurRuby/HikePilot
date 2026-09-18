import { z } from 'zod'

export const QuestionCodeSchema = z.enum([
  'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11',
])
export type QuestionCode = z.infer<typeof QuestionCodeSchema>

export const QuestionnaireAnswerInputSchema = z.object({
  question_code: QuestionCodeSchema,
  answer_value: z.string(),
})
export type QuestionnaireAnswerInput = z.infer<typeof QuestionnaireAnswerInputSchema>

export const SubmitQuestionnaireRequestSchema = z.object({
  answers: z.array(QuestionnaireAnswerInputSchema),
})
export type SubmitQuestionnaireRequest = z.infer<typeof SubmitQuestionnaireRequestSchema>

export const SuccessResponseSchema = z.object({
  success: z.literal(true),
})
export type SuccessResponse = z.infer<typeof SuccessResponseSchema>

// Background：個人條件問卷題項（specs/features/profile, recommendation 的 Background 共用）
export interface QuestionnaireQuestion {
  code: QuestionCode
  question_text: string
  answer_type: 'single_choice' | 'multi_choice' | 'open_text' | 'matrix_single_choice'
  is_required: boolean
}
