import { defineCollection, z } from 'astro:content';

const characters = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    house: z.enum(['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff', 'None']).default('None'),
    role: z.string(),
    actor: z.string().optional(),
    image: z.string().optional(),
    order: z.number().default(99),
    featured: z.boolean().default(false),
  }),
});

const books = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    number: z.number(),
    year: z.number(),
    coverImage: z.string().optional(),
    tagline: z.string().optional(),
  }),
});

const worldbuilding = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    category: z.enum(['house', 'spell', 'location', 'creature', 'object']),
    house: z.enum(['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']).optional(),
    image: z.string().optional(),
    order: z.number().default(99),
  }),
});

const upcoming = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    type: z.string(),
    releaseDate: z.string().optional(),
    teaser: z.string(),
    image: z.string().optional(),
    announced: z.boolean().default(false),
  }),
});

export const collections = { characters, books, worldbuilding, upcoming };
