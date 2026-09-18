import { z } from 'zod'

export const GeneratePlanRequestSchema = z.object({
  route_id: z.number().optional(),
})
export type GeneratePlanRequest = z.infer<typeof GeneratePlanRequestSchema>

export const SectionNameSchema = z.enum([
  '路線摘要',
  '分段行程',
  '天氣路況',
  '風險應對',
  '裝備補給',
  '交通資訊',
  '緊急應變（撤退條件、替代方案）',
  '行前 Checklist',
])
export type SectionName = z.infer<typeof SectionNameSchema>

export const PlanSectionSchema = z.object({
  section_order: z.number().min(1).max(8),
  section_name: SectionNameSchema,
})
export type PlanSection = z.infer<typeof PlanSectionSchema>

export const GeneratePlanResponseSchema = z.object({
  success: z.literal(true),
  data: z.object({
    sections: z.array(PlanSectionSchema).length(8),
    pdf_url: z.string(),
  }),
})
export type GeneratePlanResponse = z.infer<typeof GeneratePlanResponseSchema>
export type GeneratePlanData = GeneratePlanResponse['data']
