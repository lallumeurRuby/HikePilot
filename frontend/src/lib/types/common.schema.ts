import { z } from 'zod'

export const ViolationTypeSchema = z.enum([
  'UNAUTHENTICATED',
  'MISSING_REQUIRED_ANSWER',
  'INVALID_OPTION_CODE',
  'PROFILE_INCOMPLETE',
  'ROUTE_NOT_SELECTED',
  'ROUTE_NOT_IN_RECOMMENDATION',
])
export type ViolationType = z.infer<typeof ViolationTypeSchema>

export const ErrorResponseSchema = z.object({
  success: z.literal(false),
  error: z.object({
    violation_type: ViolationTypeSchema,
    message: z.string().optional(),
  }),
})
export type ErrorResponse = z.infer<typeof ErrorResponseSchema>
