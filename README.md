# 해리 포터 팬페이지

Astro 5 + Tailwind CSS v4 기반 해리 포터 팬사이트.

## 시작하기

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # dist/ 에 정적 파일 생성
npm run preview  # 빌드 결과 미리보기
```

## 페이지 구조

| 경로 | 내용 |
|---|---|
| `/` | 랜딩 페이지 |
| `/characters` | 캐릭터 목록 및 상세 |
| `/books` | 7권 시리즈 소개 |
| `/world` | 세계관 (기숙사, 장소, 마법) |
| `/upcoming` | 향후 공개 콘텐츠 |

## 콘텐츠 추가 방법

콘텐츠는 `src/content/` 아래 마크다운 파일로 관리됩니다.

### 캐릭터 추가 (`src/content/characters/`)

```markdown
---
name: 캐릭터 이름
house: Gryffindor  # Gryffindor | Slytherin | Ravenclaw | Hufflepuff | None
role: 역할
actor: 배우 이름 (선택)
order: 10          # 목록 정렬 순서
featured: false    # true면 랜딩 페이지에 노출
---

본문 내용
```

### 책 추가 (`src/content/books/`)

```markdown
---
title: 책 제목
number: 8
year: 2025
tagline: 한 줄 소개 (선택)
---

본문 내용
```

### 세계관 항목 추가 (`src/content/worldbuilding/`)

```markdown
---
title: 항목 제목
category: location  # house | spell | location | creature | object
order: 10
---

본문 내용
```

### 향후 콘텐츠 추가 (`src/content/upcoming/`)

```markdown
---
title: 콘텐츠 제목
type: 영화          # 영화 | 드라마 | 게임 | 책 등
releaseDate: 2025년 (선택)
teaser: 짧은 소개 문구
announced: true    # 공식 발표 여부
---

상세 내용
```

## 기술 스택

- **프레임워크**: [Astro 5](https://astro.build)
- **스타일링**: [Tailwind CSS v4](https://tailwindcss.com) (`@tailwindcss/vite`)
- **콘텐츠**: Astro Content Collections
- **언어**: TypeScript
