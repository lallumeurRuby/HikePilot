import type { RequestHandler } from 'msw'
// Worker adds per-resource handler imports here:
import { authHandlers } from './auth'
import { profileHandlers } from './profile'
import { recommendationHandlers } from './recommendation'
import { planHandlers } from './plan'

export const handlers: RequestHandler[] = [
  // Worker adds handler spreads here:
  ...authHandlers,
  ...profileHandlers,
  ...recommendationHandlers,
  ...planHandlers,
]
