# TTAK.KO-11.0310 AI-Ready 개정 표준초안(개정부) — JSON 형태의 자율주행 학습용 데이터 품질 검증 지침 — 정확성 및 다양성
정보통신단체표준(국문표준) · TTAK.KO-11.0310 · 제정 2022.12.07 · AI-Ready 개정 제안 · 소관 PG604 (지능형 모빌리티) · 에디터 에스에스엘㈜

> 이 초안은 **AI-Ready 개정부 중심**으로 작성되었다. 원 표준의 도메인 본문(적용범위·용어·요소 상세)은 원 표준을 계승·참조하고, AI-Ready 개정으로 새로 추가·강화되는 부분 — 인용 표준 보강(2절), 요소 정의표의 전역 어휘 식별자(4절), 기계가독 부속서(5절·부속서), 참조구현 안내(부록) — 을 실제로 채웠다. 절 번호와 양식은 「정보통신단체표준 작성지침(TTAR-09.0040)」과 그 AI-Ready 개정안(6.5.3·6.5.7·6.6·6.7)을 따른다.

> **작성 주체.** 요소 정의표의 전역 어휘 식별자(IRI) 매핑과 모든 부속서는 **에디터**가 제안 단계의 「기계가독 산출물 선언서」(별지 제11-1호서식)에 따라 작성했다(운영요령 제19조의3제1항, 작성지침 6.5.7). 별도의 공동 에디터(어휘 전문가)를 두지 아니한다. 선언과의 일치는 상정 시 자가점검표(별지 제21-1호서식) 3부에서 확인한다.

## 서문

이 표준은 「JSON 형태의 자율주행 학습용 데이터 품질 검증 지침 — 정확성 및 다양성」의 개정판이다. 원 표준(제정 2022.12.07)의 적용범위와 데이터 구조를 계승하되, 데이터를 사람과 기계가 함께 읽을 수 있도록 각 데이터 요소의 의미를 전역 어휘 식별자(IRI)에 매핑하고, 그 매핑을 JSON-LD @context로 배포하며, 값 제약·출처·품질·이용조건을 기계가독 부속서로 제공한다. 이로써 이 표준을 따르는 데이터는 별도 해석 없이 상호운용·검증·재이용이 가능해진다.

**AI-Ready 목표 수준** — 기술 대상 프로파일 ④ 품질 지표 · 필수 시맨틱 · 신태틱 (= L1) · 권장 + 품질 (DQV). (근거: 첨부 「기계가독 산출물 선언서」 및 「AI-Ready 자가점검표」)

## 1. 적용범위

이 표준은 「JSON 형태의 자율주행 학습용 데이터 품질 검증 지침 — 정확성 및 다양성」이 규정하는 데이터의 요소·구조·값 형식을 계승하며(원 표준 1절 참조), 그 데이터 요소를 전역 어휘에 매핑하여 기계가독 형식으로 배포하기 위한 요소 정의·인용 표준·부속서 구성을 규정한다. 원 표준의 도메인 규정은 변경 없이 유지되고, 이 개정은 그 위에 기계가독 계층을 더한다.

## 2. 인용 표준

다음 표준·어휘는 이 표준의 적용에 필수적이며, 본문에서 인용되는 범위에서 이 표준의 일부를 구성한다. 선언서 2에서 선언한 외부 어휘를 **모두** 등재한다(작성지침 6.5.3 · 운영요령 제19조제1항제9호). 종전에 참고 문헌에 두었던 어휘도 요소 의미가 규범적으로 의존하므로 인용 표준으로 올린다.

| 인용 표준 · 어휘 | 발행 주체 | 이 표준에서의 용도(접두어) | 사용 방식 |
|---|---|---|---|
| JSON-LD 1.1 | W3C | 요소↔IRI 매핑의 규범 직렬화(부속서 A) | 직렬화 규격 |
| Data Quality Vocabulary (DQV) | W3C | dqv: 품질 측정·차원 | IRI로 가리킴 |
| Data Catalog Vocabulary (DCAT) 3 | W3C | dcat: 데이터세트·배포본 | IRI로 가리킴 |
| DCMI Metadata Terms | DCMI | dct: 식별자·생성일·준거 | IRI로 가리킴 |
| SKOS Simple Knowledge Organization System | W3C | skos: 부속서 A에서 사용 | IRI로 가리킴 |
| Shapes Constraint Language (SHACL) | W3C | sh: 형상 적합성 | IRI로 가리킴 |
| Web Annotation Data Model | W3C | oa: 어노테이션 | IRI로 가리킴 |
| XML Schema Part 2: Datatypes | W3C | xsd: 데이터 유형(리터럴) | IRI로 가리킴 |
| ISO/IEC 5259-2 (데이터 품질 — 데이터 품질 측도) | ISO/IEC | 품질 차원 정렬(부속서 C) | 차원 이름·번호를 가리킴(정의문 전재 없음) |

> 모든 외부 어휘는 그 표준이 정의한 용어·클래스·속성·데이터 타입을 **IRI로 가리키기만** 하고 정의문을 옮겨 적지 아니한다. 따라서 작성지침 6.5.3 단서에 따라 직접 인용에 해당하지 아니하며, ISO/IEC 표준도 같은 방식으로 등재한다. 각 요소의 정의는 4절에서 **이 표준의 말로** 쓴다.

## 3. 용어, 정의 및 약어

원 표준의 용어·정의를 계승한다(원 표준 3절 참조). AI-Ready 개정으로 다음 용어를 추가한다.

| 용어 | 정의 |
|---|---|
| 전역 어휘 식별자(IRI) | 요소의 의미를 전 세계적으로 유일하게 가리키는 식별자. 이 표준은 각 요소를 하나의 IRI에 매핑한다. |
| @context | JSON 키를 IRI에 연결하는 JSON-LD 규범 매핑 파일. 부속서 A로 배포한다. |
| 프로파일 | 데이터의 성격에 따른 AI-Ready 적용 유형(① 지식정보 / ② 자기기술형 레코드 / ③ AI 데이터세트 / ④ 품질 지표). |
| 기계가독 산출물 | 데이터의 구조·의미를 정의하여 기계가 직접 처리할 수 있는 형식으로 제공하는 표준의 규범 내용(운영요령 제2조제1항제8호). 이 표준에서는 부속서로 제공한다. |
| 병행형 · 참조형 | 기계가독 산출물을 부속서에 전문 수록하고 파일로도 제공하는 형태(병행형)와, 부속서에 규범적 참조 명세를 두고 실물을 외부 저장소에 두는 형태(참조형). 작성지침 6.6. |

## 4. 데이터 요소 정의 (요소 정의표)

이 절이 AI-Ready 개정의 핵심이며, 모든 기계가독 부속서가 파생되는 원천이다. 원 표준이 정의한 데이터 요소 21개 전체를 작성지침 6.5.7의 요소 정의표로 규정한다(이 표준 필수 M 12개 · 권장 R 3개). 컬럼이 14개로 많으므로 <표 6-5>의 허용에 따라 표를 둘로 나누었다 — <표 4-1>은 값의 형식(요소 이름·표시명·데이터 유형·값 영역·다중성·필수 여부·단위), <표 4-2>는 어휘 바인딩(요소 이름·출처·버전·전역 어휘 식별자·비고)이다.

> **개정부 초안의 범위.** 14개 컬럼 가운데 **정의·기본값·예시**는 원 표준의 요소 상세를 그대로 계승하므로 이 개정부 초안에서는 생략하고, 통합본 작성 시 <표 6-5>에 따라 모두 채운다. 다중성·필수 여부는 소속 객체 기준이다(예: 파라미터 이름은 "파라미터가 있으면 반드시"). '권장'은 원 표준의 R(권장)을 뜻하며 작성지침의 필수 여부 구분(필수·선택·조건부)에서는 선택에 해당하므로 비고에 적었다.

### 4.1 객체(클래스)

요소가 소속되는 객체다. 객체는 값을 갖지 않으므로 다중성·필수 여부는 해당 없음이다.

| 객체 이름 | 표시명 | 출처 | 전역 어휘 식별자(IRI) |
|---|---|---|---|
| `Dataset` | 데이터세트 | Data Catalog Vocabulary (DCAT) 3 | `http://www.w3.org/ns/dcat#Dataset` |
| `Annotation` | 어노테이션 | Web Annotation Data Model | `http://www.w3.org/ns/oa#Annotation` |

### 4.2 요소 — 값의 형식 <표 4-1>

| 요소 이름 | 표시명 | 데이터 유형 | 값 영역 | 다중성 | 필수 여부 | 단위 |
|---|---|---|---|---|---|---|
| `datasetId` | 데이터세트 식별자 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `created` | 생성일 | 날짜 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `distribution` | 배포본 | 식별자(IRI) | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `annotations` | 어노테이션 참조 | 문자열 | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `attributes` | 속성 | 문자열 | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `label` | 라벨 | 코드 | 코드 목록(부속서 B sh:in) | 1 | 필수 | 해당 없음 |
| `type` | 어노테이션 유형 | 코드 | Bbox · Seg | 1 | 필수 | 해당 없음 |
| `size` | 크기 | 문자열 | height 200~400 · width 300~600 (원 표준 6절) | 0..1 | 선택 | 해당 없음 |
| `hasQualityMeasurement` | 품질 측정 | 식별자(IRI) | 제한 없음 | 1..n | 필수 | 해당 없음 |
| `hasDimension` | 품질 차원 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `isMeasurementOf` | 측정 대상 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `value` | 측정값 | 문자열 | 0~1 (비율) | 1 | 필수 | 비율(0~1) |
| `syntaxAccuracy` | 구문 정확성 | 식별자(IRI) | 0.99~1.0 — 원 표준 품질목표 99% 이상 | 1 | 필수 | 비율(0~1) |
| `statSufficiency` | 통계 충분성 | 식별자(IRI) | 0~1 (비율) | 1 | 필수 | 비율(0~1) |
| `statUniformity` | 통계 균일성 | 식별자(IRI) | 0~1 (비율) | 1 | 필수 | 비율(0~1) |
| `accuracy` | 정확성 차원 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `diversity` | 다양성 차원 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `conformsTo` | 준거 스키마 | 식별자(IRI) | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `shape` | 형상 적합 | 불리언 | 제한 없음 | 0..1 | 선택 | 해당 없음 |

### 4.3 요소 — 어휘 바인딩 <표 4-2>

전역 어휘 식별자(IRI) 컬럼은 에디터가 선언서 2의 어휘 범위 안에서 작성했다. 자체 정의 요소는 '자체 정의'로 적고 비고에 이 표준의 네임스페이스 IRI를 밝힌다. 직렬화 키(@context의 키)는 요소 이름과 같다.

| 요소 이름 | 출처 | 버전 | 전역 어휘 식별자(IRI) | 비고 |
|---|---|---|---|---|
| `datasetId` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/identifier` | 해당 없음 |
| `created` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/created` | 권장 |
| `distribution` | Data Catalog Vocabulary (DCAT) 3 | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dcat#distribution` | 권장 |
| `annotations` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#hasAnnotation` |
| `attributes` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#attributes` |
| `label` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#label` |
| `type` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#annotationType` |
| `size` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#size` |
| `hasQualityMeasurement` | Data Quality Vocabulary (DQV) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dqv#hasQualityMeasurement` | 해당 없음 |
| `hasDimension` | Data Quality Vocabulary (DQV) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dqv#inDimension` | 해당 없음 |
| `isMeasurementOf` | Data Quality Vocabulary (DQV) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dqv#isMeasurementOf` | 해당 없음 |
| `value` | Data Quality Vocabulary (DQV) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dqv#value` | 해당 없음 |
| `syntaxAccuracy` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#syntaxAccuracy` · 값은 dqv:QualityMeasurement 노드 |
| `statSufficiency` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#statisticalSufficiency` · 값은 dqv:QualityMeasurement 노드 |
| `statUniformity` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#statisticalUniformity` · 값은 dqv:QualityMeasurement 노드 |
| `accuracy` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#AccuracyDimension` |
| `diversity` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/adq#DiversityDimension` |
| `conformsTo` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/conformsTo` | 권장 |
| `shape` | Shapes Constraint Language (SHACL) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/shacl#conforms` | 해당 없음 |

### 4.4 코드·열거값

코드(열거) 유형 요소의 허용값이다. 부속서의 SHACL 형상에서 `sh:in` 제약으로 검증한다.

| 요소 | 허용값 목록 |
|---|---|
| 어노테이션 타입(adq:annotationType) | Bbox · Seg |

### 4.6 형상 전체에 걸리는 값 제약

요소 하나에 대응하지 않는 규칙(택일·범위 조합·특정 노드 대상)은 요소 정의표가 아니라 여기에 적고, SHACL 형상에서 `sh:or`·`sh:targetNode` 등으로 표현한다.

| 적용 대상 | 값 범위 · 유효 조건 |
|---|---|
| 어노테이션 타입 | type은 Bbox·Seg 중 하나여야 함(유효값 오류) |
| 이미지 높이 | size(height)는 200~400 범위(유효 범위 오류) |
| 이미지 너비 | size(width)는 300~600 범위(유효 범위 오류) |
| dqv:value | 구문 정확성은 0.99(99%) 이상이어야 함 |

## 5. 기계가독 산출물 및 부속서

이 표준을 따르는 데이터의 기계가독 표현은 다음 부속서로 제공한다(운영요령 제19조의3, 작성지침 6.6). 요소 정의표는 4절 본문이며 부속서가 아니다. 별표(★)는 이 표준의 기술 대상 프로파일에서 필수 산출물이다.

| 부속서 | 산출물 | 구성요소 | 형태 | 제공 파일 | 필수/권장 |
|---|---|---|---|---|---|
| 부속서 A | JSON-LD @context | ② 신태틱 | 병행형(작성지침 6.6 a) | `부속서/부속서A_TTAK.KO-11.0310_context.jsonld` | ★ 필수 |
| 부속서 B | SHACL 형상(값 제약 검증) | ③ 데이터 모델 | 병행형(작성지침 6.6 a) | `부속서/부속서B_TTAK.KO-11.0310_shapes.ttl` | 권장 |
| 부속서 C | DQV 품질 측도 | ⑥ 품질 측도 | 병행형(작성지침 6.6 a) | `부속서/부속서C_TTAK.KO-11.0310_quality.ttl` | 권장 |

**형태.** 병행형 부속서는 부속서에 전문을 수록하고 같은 내용을 파일로도 제공한다. **수록본이 정본**이며 파일은 기계가 직접 처리하기 위한 것이다. 어느 형태이든 파일 자체에 이용조건을 표시했다(5.1).

### 5.1 산출물의 이용조건

이 표준이 제공하는 모든 기계가독 산출물의 이용조건은 **CC BY 4.0**(https://creativecommons.org/licenses/by/4.0/)이다. Turtle 파일은 머리말 주석과 `<> dcterms:license` 트리플로, JSON-LD 파일은 최상위 `$comment` 키와 `http://purl.org/dc/terms/license` 키로 파일 안에 표시했다. 이는 **산출물 자체**의 이용조건이며, 이 표준을 따라 쌓이는 데이터의 이용조건(원 표준의 권리 요소)과는 별개다.

### 5.2 부속서 번호

부속서 번호는 작성지침 6.6의 A, B, C 순 부여 원칙에 따른다. 원 표준에 부속서가 있으면 그다음 알파벳부터 부여하며, 이 개정부 초안은 작성 편의상 A부터 적었다. 기계가독 산출물이라 하여 특정 알파벳을 고정하지 아니한다.

## 부속서 A JSON-LD @context

**(본 부속서는 표준 내용의 일부임)**

### A.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ② 신태틱의 증빙이다.

### A.2 설계

4절 요소 정의표의 요소 이름을 키로, 전역 어휘 식별자(IRI)를 값으로 하는 JSON-LD 1.1 @context다. <표 4-2>와 1:1로 대응하며, 자체 정의 요소는 이 표준의 네임스페이스로 전개된다. 네임스페이스 접두어는 다음과 같다.

| 접두어 | 네임스페이스 IRI |
|---|---|
| dqv | `http://www.w3.org/ns/dqv#` |
| dcat | `http://www.w3.org/ns/dcat#` |
| dct | `http://purl.org/dc/terms/` |
| skos | `http://www.w3.org/2004/02/skos/core#` |
| sh | `http://www.w3.org/ns/shacl#` |
| oa | `http://www.w3.org/ns/oa#` |
| adq | `https://std.tta.or.kr/ns/adq#` |
| xsd | `http://www.w3.org/2001/XMLSchema#` |

### A.3 수록본 (병행형 · 정본)

파일 `부속서/부속서A_TTAK.KO-11.0310_context.jsonld`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
{
  "$comment": "TTAK.KO-11.0310 부속서 A — JSON-LD @context (본 부속서는 표준 내용의 일부임). 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/. 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다(운영요령 제19조의3제2항). 근거: 운영요령 제19조의3제7항, 작성지침 6.6.",
  "http://purl.org/dc/terms/license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "@context": {
    "@version": 1.1,
    "dqv": "http://www.w3.org/ns/dqv#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "sh": "http://www.w3.org/ns/shacl#",
    "oa": "http://www.w3.org/ns/oa#",
    "adq": "https://std.tta.or.kr/ns/adq#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "Dataset": "dcat:Dataset",
    "Annotation": "oa:Annotation",

    "datasetId": { "@id": "dct:identifier", "@type": "@id" },
    "created": { "@id": "dct:created", "@type": "xsd:date" },
    "distribution": { "@id": "dcat:distribution", "@type": "@id" },

    "annotations": { "@id": "adq:hasAnnotation", "@container": "@set" },
    "attributes": "adq:attributes",
    "label": { "@id": "adq:label", "@type": "@vocab" },
    "type": { "@id": "adq:annotationType", "@type": "@vocab" },
    "size": "adq:size",

    "hasQualityMeasurement": { "@id": "dqv:hasQualityMeasurement", "@type": "@id" },
    "hasDimension": { "@id": "dqv:inDimension", "@type": "@id" },
    "isMeasurementOf": { "@id": "dqv:isMeasurementOf", "@type": "@id" },
    "value": "dqv:value",

    "syntaxAccuracy": { "@id": "adq:syntaxAccuracy", "@type": "dqv:QualityMeasurement" },
    "statSufficiency": { "@id": "adq:statisticalSufficiency", "@type": "dqv:QualityMeasurement" },
    "statUniformity": { "@id": "adq:statisticalUniformity", "@type": "dqv:QualityMeasurement" },

    "accuracy": "adq:AccuracyDimension",
    "diversity": "adq:DiversityDimension",

    "conformsTo": { "@id": "dct:conformsTo", "@type": "@id" },
    "shape": { "@id": "sh:conforms", "@type": "xsd:boolean" }
  },
  "_meta": {
    "standard": "TTAK.KO-11.0310",
    "title": "JSON 형태의 자율주행 학습용 데이터 품질 검증 지침 — 정확성 및 다양성",
    "profile": "③ AI 데이터세트(품질 블록)",
    "note": "정확성(구문)·다양성(통계) 지표를 DQV QualityMeasurement로, 검증 규칙(구조·타입·유효범위)을 SHACL sh:conforms로 형식화 → 검증 자동생성 트랙 직결. adq 접두어는 자율주행 데이터품질 확장 네임스페이스. 품질 모델은 ISO/IEC 5259-2 정렬 권장."
  }
}
```

### A.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서A_TTAK.KO-11.0310_context.jsonld` |
| 형식 | JSON-LD |
| 무결성 확인 값 | `sha256:3e2ab45d86d1d338a4bf1f591924e7371e625bcae89f6cb893422ff3b44a6851` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 B SHACL 형상(값 제약 검증)

**(본 부속서는 표준 내용의 일부임)**

### B.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ③ 데이터 모델의 증빙이다.

### B.2 설계

4절 요소 정의표의 필수 여부·다중성·값 영역을 SHACL 형상으로 옮긴 것이다. 필수 여부와 다중성은 `sh:minCount`·`sh:maxCount`로, 값 범위는 `sh:minInclusive`·`sh:maxInclusive`로, 허용값(코드)은 `sh:in`으로, 길이·형식은 `sh:pattern`·`sh:minLength`·`sh:maxLength`로, 단위는 `sh:hasValue` 또는 `sh:in`으로 대응한다. 형상 전체에 걸리는 규칙(4.6)은 `sh:or`·`sh:closed`·`sh:targetNode`로 표현한다. 요소 정의표를 고치면 이 형상을 다시 생성한다.

### B.3 수록본 (병행형 · 정본)

파일 `부속서/부속서B_TTAK.KO-11.0310_shapes.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-11.0310 부속서 B — SHACL 형상(값 제약 검증)  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# SHACL 검증 스키마 — TTAK.KO-11.0310
# 재생성: 요소 정의표(원천)의 M(필수)/R/O·카디널리티로 minCount/maxCount 구동.
# 값 제약(이미지 크기 허용범위·구문 정확성 목표)은 원 표준 6절 표 및 품질목표 99%에서 옮긴다.

@prefix adq: <https://std.tta.or.kr/ns/adq#> .
@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dcam: <http://purl.org/dc/dcam/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcmitype: <http://purl.org/dc/dcmitype/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix oa: <http://www.w3.org/ns/oa#> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qb: <http://purl.org/linked-data/cube#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix vann: <http://purl.org/vocab/vann/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix wgs: <https://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dcterms:license <https://creativecommons.org/licenses/by/4.0/> .

adq:AnnotationShape a sh:NodeShape ;
  sh:targetClass oa:Annotation ;
  sh:property [ sh:path adq:annotationType ; sh:name "어노테이션 타입" ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( "Bbox" "Seg" ) ; sh:message "type은 Bbox·Seg 중 하나여야 함(유효값 오류)" ] ;
  sh:property [ sh:path adq:attributes ; sh:name "객체 소분류/속성" ] ;
  sh:property [ sh:path adq:id ; sh:name "어노테이션ID" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path adq:label ; sh:name "객체 대분류" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path adq:sizeHeight ; sh:name "이미지 높이" ; sh:minCount 1 ; sh:datatype xsd:integer ; sh:minInclusive 200 ; sh:maxInclusive 400 ; sh:message "size(height)는 200~400 범위(유효 범위 오류)" ] ;
  sh:property [ sh:path adq:sizeWidth ; sh:name "이미지 너비" ; sh:minCount 1 ; sh:datatype xsd:integer ; sh:minInclusive 300 ; sh:maxInclusive 600 ; sh:message "size(width)는 300~600 범위(유효 범위 오류)" ] .

adq:QualityProfileShape a sh:NodeShape ;
  sh:targetClass dqv:QualityMeasurement ;
  sh:property [ sh:path dqv:isMeasurementOf ; sh:name "품질지표" ; sh:minCount 1 ; sh:maxCount 1 ; sh:nodeKind sh:IRI ] ;
  sh:property [ sh:path dqv:value ; sh:name "측정값" ; sh:minCount 1 ; sh:maxCount 1 ] .

adq:SyntaxAccuracyShape a sh:NodeShape ;
  # sh:targetNode 가 없으면 이 형상은 어떤 노드에도 걸리지 않아 검증에서 통째로 빠진다.
  sh:targetNode adq:syntaxAccuracy ;
  sh:property [ sh:path dqv:value ; sh:minCount 1 ; sh:maxCount 1 ; sh:minInclusive 0.99 ; sh:maxInclusive 1.0 ; sh:message "구문 정확성은 0.99(99%) 이상이어야 함 (원 표준 품질목표)" ] .
```

### B.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서B_TTAK.KO-11.0310_shapes.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:5a3985c754ac77332bb85d019bb8229af039f170ed0c24182ef1b4a49e3092ad` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 C DQV 품질 측도

**(본 부속서는 표준 내용의 일부임)**

### C.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ⑥ 품질 측도의 증빙이다.

### C.2 설계

품질을 `dqv:QualityMeasurement`로 형식화하고, 각 측정을 품질 차원(ISO/IEC 5259-2 정렬)에 연결한다. 차원은 이름과 번호로 가리키기만 하고 정의문을 옮겨 적지 아니한다. 예시 측정값은 부속서의 예시 데이터세트 측정치이며 표준이 특정 수치를 규정하지 않는다.

| 품질 차원 (isMeasurementOf) | 예시 측정값 (부속서 C) | 설명 |
|---|---|---|
| syntacticAccuracyRate | 0.95 | 제공 10,000건 중 오류 500건 → 0.95 (품질목표 0.99 미달, 재수행 필요) |
| classCoverage | 7 | 총 분류체계 7종, 각 클래스 인스턴스 수량 확보 |
| classBalanceIndex | 0.86 | 위반유형 7종 분포 10~17.5% → 균형 지수 0.86 |
| diversityScore | 0.82 |  |

### C.3 수록본 (병행형 · 정본)

파일 `부속서/부속서C_TTAK.KO-11.0310_quality.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-11.0310 부속서 C — DQV 품질 측도  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# DQV 품질 프로파일 — TTAK.KO-11.0310 (자율주행 학습데이터, 품질 L3)
# 본 표준의 '정확성(구문)·다양성(통계 충분성·균일성)'을 ISO/IEC 5259-2 차원에 정렬해 dqv:QualityMeasurement로 형식화.
# → 검증 자동생성 트랙(SHACL) 및 품질목표(99%)와 직결.
@prefix dqv:     <http://www.w3.org/ns/dqv#> .
@prefix dcat:    <http://www.w3.org/ns/dcat#> .
@prefix dct:     <http://purl.org/dc/terms/> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix iso5259: <https://std.tta.or.kr/ns/iso5259-2#> .
@prefix ex:      <https://example.org/adq/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

ex:autonomous-dataset a dcat:Dataset ;
  dct:title "자율자동차 안전 위험 시설물 데이터" ;
  dct:conformsTo "TTAK.KO-11.0310" ;
  dqv:hasQualityMeasurement ex:m-accuracy, ex:m-sufficiency, ex:m-balance, ex:m-diversity .

# 구문 정확성 (오류율 기반, 목표 ≥ 0.99)
ex:m-accuracy a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:syntacticAccuracyRate ;
  dqv:computedOn ex:autonomous-dataset ;
  dqv:value "0.950"^^xsd:double ;
  dct:description "제공 10,000건 중 오류 500건 → 0.95 (품질목표 0.99 미달, 재수행 필요)" .

# 통계적 충분성 (분류체계별 수량)
ex:m-sufficiency a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:classCoverage ;
  dqv:computedOn ex:autonomous-dataset ;
  dqv:value "7"^^xsd:integer ;
  dct:description "총 분류체계 7종, 각 클래스 인스턴스 수량 확보" .

# 통계적 균일성 (클래스 균형)
ex:m-balance a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:classBalanceIndex ;
  dqv:computedOn ex:autonomous-dataset ;
  dqv:value "0.86"^^xsd:double ;
  dct:description "위반유형 7종 분포 10~17.5% → 균형 지수 0.86" .

# 다양성
ex:m-diversity a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:diversityScore ;
  dqv:computedOn ex:autonomous-dataset ;
  dqv:value "0.82"^^xsd:double .
```

### C.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서C_TTAK.KO-11.0310_quality.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:25ad596f35ad03f6572c7df0f23ec0909e143e80e5244a13849505f496b1b917` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부록 (자유 작성) 참조구현 안내

이 표준은 참조구현을 공개하지 아니한다. 향후 공개하는 경우 이 부록에 위치·언어·라이선스를 적고, 참조구현은 표준의 일부가 아니며 협회는 그 내용에 대하여 보증하지 아니한다는 문구를 함께 둔다(운영요령 제19조의3제8항).

## 부록 (자유 작성) 원 표준 대비 교정 사항

원 표준의 현행 진단에서 확인된 정합성 결함(1건 — DQV 용어 오용 1건(dqv:Measurement를 값 타입으로 사용))을 이 개정에서 본문·부속서로 교정했다. 교정 결과는 자가점검표 2부에 적었다.
