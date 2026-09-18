import { z } from 'zod'

export const RouteSummarySchema = z.object({
  route_id: z.number(),
  name: z.string(),
})
export type RouteSummary = z.infer<typeof RouteSummarySchema>

export const RecommendationResponseSchema = z.object({
  success: z.literal(true),
  data: z.object({
    has_matches: z.boolean(),
    routes: z.array(RouteSummarySchema).max(3),
  }),
})
export type RecommendationResponse = z.infer<typeof RecommendationResponseSchema>
export type RecommendationData = RecommendationResponse['data']
