# Project Context

## 기술 스택
- **프레임워크**: Astro 5
- **스타일링**: Tailwind CSS v4 (`@tailwindcss/vite` 플러그인)
- **언어**: TypeScript
- **콘텐츠**: Astro Content Collections (`.md` / `.mdx`)

## 아키텍처

```
src/
  ├── pages/           (라우팅)
  ├── components/      (UI 컴포넌트)
  ├── layouts/         (레이아웃 템플릿)
  ├── content/         (Content Collections)
  │   ├── characters/
  │   ├── books/
  │   ├── worldbuilding/
  │   └── config.ts
  ├── styles/          (global.css)
  └── assets/          (이미지 등)
public/                (정적 자산)
```

## 코드 컨벤션
- Tailwind v4: `global.css`에 `@import "tailwindcss"` 선언
- Content Collections: `defineCollection()` + zod 스키마
- 동적 라우트: `[slug].astro` 패턴

## 환경 정보
- 로컬 서버: `npm run dev` (기본 포트 4321)
- 빌드: `npm run build`
- 프리뷰: `npm run preview`

## 설계 원칙
- 콘텐츠 데이터는 마크다운 파일로 관리 (Content Collections)
- 향후 콘텐츠 확장을 위한 `upcoming/` 컬렉션 포함
- 모바일 반응형 우선 설계
