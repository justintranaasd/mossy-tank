import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Hand-written articles (Markdown/MDX) live in src/content/blog.
const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    // Maps to the content clusters in the plan.
    cluster: z
      .enum(['low-tech', 'betta', 'shrimp-nano', 'plants', 'troubleshooting', 'gear', 'general'])
      .default('general'),
    // Page role: pillar hub, info post, money/affiliate, troubleshooting, page.
    pageType: z.enum(['pillar', 'info', 'money', 'trouble', 'page']).default('info'),
    heroImage: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

// Programmatic plant care pages (Phase 2) — dataset-driven. Stub for now.
const plants = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/plants' }),
  schema: z.object({
    commonName: z.string(),
    scientificName: z.string(),
    difficulty: z.enum(['easy', 'medium', 'advanced']),
    light: z.enum(['low', 'medium', 'high']),
    co2: z.enum(['not-needed', 'optional', 'required']),
    placement: z.enum(['foreground', 'midground', 'background', 'floating', 'carpet', 'epiphyte']),
    growthRate: z.enum(['slow', 'moderate', 'fast']).optional(),
    tempRange: z.string().optional(),
    phRange: z.string().optional(),
    summary: z.string(),
  }),
});

export const collections = { blog, plants };
