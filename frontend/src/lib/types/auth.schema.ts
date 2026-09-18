import { z } from 'zod'

export const GoogleLoginRequestSchema = z.object({
  google_id: z.string(),
  email: z.string().email(),
  name: z.string(),
})
export type GoogleLoginRequest = z.infer<typeof GoogleLoginRequestSchema>

export const GoogleLoginResponseSchema = z.object({
  success: z.literal(true),
  data: z.object({
    is_new_user: z.boolean(),
    token: z.string(),
    next_step: z.enum(['questionnaire']).optional(),
  }),
})
export type GoogleLoginResponse = z.infer<typeof GoogleLoginResponseSchema>
export type GoogleLoginData = GoogleLoginResponse['data']
