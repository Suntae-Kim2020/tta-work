# TTAK.KO-10.1594 AI-Ready 개정 표준초안(개정부) — AI 모델의 학습 데이터세트 관리와 상호운용성 지원을 위한 메타데이터
정보통신단체표준(국문표준) · TTAK.KO-10.1594 · 제정 2025.12.05 · AI-Ready 개정 제안 · 소관 PG606 (인공지능 기반기술) · 에디터 국립군산대학교 · 제안자 KISTI

> 이 초안은 **AI-Ready 개정부 중심**으로 작성되었다. 원 표준의 도메인 본문(적용범위·용어·요소 상세)은 원 표준을 계승·참조하고, AI-Ready 개정으로 새로 추가·강화되는 부분 — 인용 표준 보강(2절), 요소 정의표의 전역 어휘 식별자(4절), 기계가독 부속서(5절·부속서), 참조구현 안내(부록) — 을 실제로 채웠다. 절 번호와 양식은 「정보통신단체표준 작성지침(TTAR-09.0040)」과 그 AI-Ready 개정안(6.5.3·6.5.7·6.6·6.7)을 따른다.

> **작성 주체.** 요소 정의표의 전역 어휘 식별자(IRI) 매핑과 모든 부속서는 **에디터**가 제안 단계의 「기계가독 산출물 선언서」(별지 제11-1호서식)에 따라 작성했다(운영요령 제19조의3제1항, 작성지침 6.5.7). 별도의 공동 에디터(어휘 전문가)를 두지 아니한다. 선언과의 일치는 상정 시 자가점검표(별지 제21-1호서식) 3부에서 확인한다.

## 서문

이 표준은 「AI 모델의 학습 데이터세트 관리와 상호운용성 지원을 위한 메타데이터」의 개정판이다. 원 표준(제정 2025.12.05)의 적용범위와 데이터 구조를 계승하되, 데이터를 사람과 기계가 함께 읽을 수 있도록 각 데이터 요소의 의미를 전역 어휘 식별자(IRI)에 매핑하고, 그 매핑을 JSON-LD @context로 배포하며, 값 제약·출처·품질·이용조건을 기계가독 부속서로 제공한다. 이로써 이 표준을 따르는 데이터는 별도 해석 없이 상호운용·검증·재이용이 가능해진다.

**AI-Ready 목표 수준** — 기술 대상 프로파일 ③ AI 데이터세트 (모델·학습 데이터 통합 기술) · 필수 시맨틱 · 신태틱 · 데이터 모델 · 출처 (= L2) · 권장 + 운영 · 품질 · 접근 (= L3). (근거: 첨부 「기계가독 산출물 선언서」 및 「AI-Ready 자가점검표」)

## 1. 적용범위

이 표준은 「AI 모델의 학습 데이터세트 관리와 상호운용성 지원을 위한 메타데이터」이 규정하는 데이터의 요소·구조·값 형식을 계승하며(원 표준 1절 참조), 그 데이터 요소를 전역 어휘에 매핑하여 기계가독 형식으로 배포하기 위한 요소 정의·인용 표준·부속서 구성을 규정한다. 원 표준의 도메인 규정은 변경 없이 유지되고, 이 개정은 그 위에 기계가독 계층을 더한다.

## 2. 인용 표준

다음 표준·어휘는 이 표준의 적용에 필수적이며, 본문에서 인용되는 범위에서 이 표준의 일부를 구성한다. 선언서 2에서 선언한 외부 어휘를 **모두** 등재한다(작성지침 6.5.3 · 운영요령 제19조제1항제9호). 종전에 참고 문헌에 두었던 어휘도 요소 의미가 규범적으로 의존하므로 인용 표준으로 올린다.

| 인용 표준 · 어휘 | 발행 주체 | 이 표준에서의 용도(접두어) | 사용 방식 |
|---|---|---|---|
| JSON-LD 1.1 | W3C | 요소↔IRI 매핑의 규범 직렬화(부속서 A) | 직렬화 규격 |
| DCMI Metadata Terms | DCMI | dct: 식별자·설명·발행일·라이선스 | IRI로 가리킴 |
| Data Catalog Vocabulary (DCAT) 3 | W3C | dcat: 데이터세트·배포본 | IRI로 가리킴 |
| SKOS Simple Knowledge Organization System | W3C | skos: 과업 분류 | IRI로 가리킴 |
| schema.org | Schema.org | schema: 소프트웨어 버전 | IRI로 가리킴 |
| PROV-O: The PROV Ontology | W3C | prov: 모델 파생 기원 | IRI로 가리킴 |
| QUDT Schema | QUDT.org | qudt: 평가지표 단위 | IRI로 가리킴 |
| QUDT Units Vocabulary | QUDT.org | unit: 부속서 B·C에서 사용 | IRI로 가리킴 |
| Data Quality Vocabulary (DQV) | W3C | dqv: 부속서 F에서 사용 | IRI로 가리킴 |
| ODRL Information Model 2.2 | W3C | odrl: 부속서 G에서 사용 | IRI로 가리킴 |
| Data Use Ontology (DUO) | OBO Foundry | duo: 부속서 G에서 사용 | IRI로 가리킴 |
| Shapes Constraint Language (SHACL) | W3C | sh: 값 검증 언어 — 부속서 B | IRI로 가리킴 |
| Croissant ML Metadata 1.0 | MLCommons | cr: 부속서 E에서 사용 | IRI로 가리킴 |
| XML Schema Part 2: Datatypes | W3C | xsd: 데이터 유형(리터럴) | IRI로 가리킴 |
| ISO/IEC 5259-2 (데이터 품질 — 데이터 품질 측도) | ISO/IEC | 품질 차원 정렬(부속서 F) | 차원 이름·번호를 가리킴(정의문 전재 없음) |

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

이 절이 AI-Ready 개정의 핵심이며, 모든 기계가독 부속서가 파생되는 원천이다. 원 표준이 정의한 데이터 요소 50개 전체를 작성지침 6.5.7의 요소 정의표로 규정한다(이 표준 필수 M 17개 · 권장 R 7개). 컬럼이 14개로 많으므로 <표 6-5>의 허용에 따라 표를 둘로 나누었다 — <표 4-1>은 값의 형식(요소 이름·표시명·데이터 유형·값 영역·다중성·필수 여부·단위), <표 4-2>는 어휘 바인딩(요소 이름·출처·버전·전역 어휘 식별자·비고)이다.

> **개정부 초안의 범위.** 14개 컬럼 가운데 **정의·기본값·예시**는 원 표준의 요소 상세를 그대로 계승하므로 이 개정부 초안에서는 생략하고, 통합본 작성 시 <표 6-5>에 따라 모두 채운다. 다중성·필수 여부는 소속 객체 기준이다(예: 파라미터 이름은 "파라미터가 있으면 반드시"). '권장'은 원 표준의 R(권장)을 뜻하며 작성지침의 필수 여부 구분(필수·선택·조건부)에서는 선택에 해당하므로 비고에 적었다.

### 4.1 객체(클래스)

요소가 소속되는 객체다. 객체는 값을 갖지 않으므로 다중성·필수 여부는 해당 없음이다.

| 객체 이름 | 표시명 | 출처 | 전역 어휘 식별자(IRI) |
|---|---|---|---|
| `AIModel` | AI 모델 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#AIModel`) |
| `Dataset` | 데이터세트 | Data Catalog Vocabulary (DCAT) 3 | `http://www.w3.org/ns/dcat#Dataset` |
| `Task` | 과업 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#Task`) |
| `Metric` | 평가지표 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#Metric`) |
| `Parameter` | 파라미터 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#Parameter`) |
| `HyperParameter` | 하이퍼파라미터 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#HyperParameter`) |
| `ModelDerivation` | 모델 파생 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#ModelDerivation`) |
| `Document` | 문서 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#Document`) |

### 4.2 요소 — 값의 형식 <표 4-1>

| 요소 이름 | 표시명 | 데이터 유형 | 값 영역 | 다중성 | 필수 여부 | 단위 |
|---|---|---|---|---|---|---|
| `unit` | 단위(공통) | 코드 | 지표 unit:PERCENT · NUM · UNITLESS / 파라미터는 여기에 unit:SEC 추가 | 0..1 | 선택 | 해당 없음 |
| `identifier` | 식별자 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `modelName` | 모델명 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `description` | 설명 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `modelArchitecture` | 모델 구조 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `framework` | 프레임워크 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `softwareVersion` | SW 버전 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `releaseDate` | 공개일 | 날짜시간 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `license` | 라이선스 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `organization` | 기관 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `modelSize` | 모델 크기 | 문자열 | 제한 없음 | 0..1 | 선택 | MB |
| `hasTask` | 과업 참조 | 식별자(IRI) | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `hasDocument` | 문서 참조 | 식별자(IRI) | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `TrainingSet` | 학습 분할 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `ValidationSet` | 검증 분할 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `TestSet` | 시험 분할 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `trainingData` | 학습 데이터 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `hasEvaluationMetric` | 평가지표 참조 | 식별자(IRI) | 제한 없음 | 1..n | 필수 | 해당 없음 |
| `hasTrainingProcess` | 학습 과정 | 식별자(IRI) | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `hasDerivativeRelation` | 파생 관계 | 식별자(IRI) | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `derivativeModel` | 파생 모델 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `derivativeMethod` | 파생 방법 | 문자열 | Finetune · Distill · Merge | 1 | 필수 | 해당 없음 |
| `wasDerivedFrom` | 파생 기원 | 식별자(IRI) | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `taskCategory` | 과업 분류 | 코드 | 코드 목록(부속서 B sh:in) | 0..1 | 선택 | 해당 없음 |
| `metricName` | 지표명 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `hasFormula` | 산식 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `preferredDirection` | 선호 방향 | 코드 | maximize · minimize (값이 클수록 좋은 지표인가) | 0..1 | 선택 | 해당 없음 |
| `parameterName` | 파라미터명 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `parameterValue` | 파라미터 값 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `parameterType` | 파라미터 유형 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `usedForPhase` | 사용 단계 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `tunable` | 조정 가능 | 불리언 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `defaultValue` | 기본값 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `recommendedRange` | 권장 범위 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `unitCode` | 단위 코드 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `metricUnit` | 지표 단위 | 코드 | unit:PERCENT · NUM · UNITLESS (백분율 · 점수/개수 · 0~1 비율) | 0..1 | 선택 | 지표별(부속서 C) |
| `metricUnitCode` | 지표 단위 코드 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `distribution` | 배포본 | 식별자(IRI) | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `keyword` | 키워드 | 문자열 | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `theme` | 주제 | 식별자(IRI) | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `created` | 생성일 | 날짜시간 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `modified` | 수정일 | 날짜시간 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `accessRights` | 접근 권한 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |

### 4.3 요소 — 어휘 바인딩 <표 4-2>

전역 어휘 식별자(IRI) 컬럼은 에디터가 선언서 2의 어휘 범위 안에서 작성했다. 자체 정의 요소는 '자체 정의'로 적고 비고에 이 표준의 네임스페이스 IRI를 밝힌다. 직렬화 키(@context의 키)는 요소 이름과 같다.

| 요소 이름 | 출처 | 버전 | 전역 어휘 식별자(IRI) | 비고 |
|---|---|---|---|---|
| `unit` | QUDT Schema | 이번 AI-Ready 개정판 | `http://qudt.org/schema/qudt/unit` | 해당 없음 |
| `identifier` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/identifier` | 해당 없음 |
| `modelName` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#modelName` |
| `description` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/description` | 권장 |
| `modelArchitecture` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#modelArchitecture` |
| `framework` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#framework` · 권장 |
| `softwareVersion` | schema.org | 이번 AI-Ready 개정판 | `https://schema.org/softwareVersion` | 해당 없음 |
| `releaseDate` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/issued` | 권장 |
| `license` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/license` | 해당 없음 |
| `organization` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#organization` · 권장 |
| `modelSize` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#modelSize` |
| `hasTask` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#hasTask` |
| `hasDocument` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#hasDocument` |
| `TrainingSet` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#TrainingSet` |
| `ValidationSet` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#ValidationSet` |
| `TestSet` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#TestSet` |
| `trainingData` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#trainingData` |
| `hasEvaluationMetric` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#hasEvaluationMetric` |
| `hasTrainingProcess` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#hasTrainingProcess` |
| `hasDerivativeRelation` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#hasDerivativeRelation` |
| `derivativeModel` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#derivativeModel` |
| `derivativeMethod` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#derivativeMethod` |
| `wasDerivedFrom` | PROV-O: The PROV Ontology | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/prov#wasDerivedFrom` | 권장 |
| `taskCategory` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#taskCategory` |
| `metricName` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#metricName` |
| `hasFormula` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#hasFormula` |
| `preferredDirection` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#preferredDirection` |
| `parameterName` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#parameterName` |
| `parameterValue` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#parameterValue` |
| `parameterType` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#parameterType` |
| `usedForPhase` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#usedForPhase` |
| `tunable` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#tunable` |
| `defaultValue` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#defaultValue` |
| `recommendedRange` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#recommendedRange` |
| `unitCode` | QUDT Schema | 이번 AI-Ready 개정판 | `http://qudt.org/schema/qudt/ucumCode` | 리터럴 유형 qudt:UCUMcs |
| `metricUnit` | QUDT Schema | 이번 AI-Ready 개정판 | `http://qudt.org/schema/qudt/unit` | 권장 |
| `metricUnitCode` | QUDT Schema | 이번 AI-Ready 개정판 | `http://qudt.org/schema/qudt/ucumCode` | 리터럴 유형 qudt:UCUMcs |
| `distribution` | Data Catalog Vocabulary (DCAT) 3 | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dcat#distribution` | 해당 없음 |
| `keyword` | Data Catalog Vocabulary (DCAT) 3 | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dcat#keyword` | 해당 없음 |
| `theme` | Data Catalog Vocabulary (DCAT) 3 | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dcat#theme` | 해당 없음 |
| `created` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/created` | 해당 없음 |
| `modified` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/modified` | 해당 없음 |
| `accessRights` | Data Catalog Vocabulary (DCAT) 3 | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/dcat#accessRights` | 권장 |

### 4.4 코드·열거값

코드(열거) 유형 요소의 허용값이다. 부속서의 SHACL 형상에서 `sh:in` 제약으로 검증한다.

| 요소 | 허용값 목록 |
|---|---|
| koai:derivativeMethod(koai:derivativeMethod) | Finetune · Distill · Merge |
| koai:preferredDirection(koai:preferredDirection) | maximize · minimize |

### 4.5 단위

측정값 요소의 단위를 QUDT 단위 IRI(규범)와 UCUM 코드(비-RDF 소비자용)에 함께 결합한다(작성지침 부속서 B.4). 단위 부속서에 같은 내용을 기계가독 형식으로 둔다.

| 단위(표기) | QUDT 단위 IRI | UCUM 코드 | 적용 범위 |
|---|---|---|---|
| % | `unit:PERCENT` | % | 표 6-7). ucumCode는 QUDT 공식값. |
| sec | `unit:SEC` | s | 원문 표기: 'sec'(표 6-5). UCUM 정규 |
| 개수 | `unit:NUM` | {#} | 차원 없는 개수. QUDT qudt:Counting |
| tokens | `unit:NUM` | {tokens} | 원문 표기: 'tokens'(표 6-5 예시). 단 |
| 점수 | `unit:NUM` | {score} | hasFormula가 지시한다. ucumCode '{score}'는 UCUM 주석 문법으로 조성한 값이다. |

### 4.6 형상 전체에 걸리는 값 제약

요소 하나에 대응하지 않는 규칙(택일·범위 조합·특정 노드 대상)은 요소 정의표가 아니라 여기에 적고, SHACL 형상에서 `sh:or`·`sh:targetNode` 등으로 표현한다.

| 적용 대상 | 값 범위 · 유효 조건 |
|---|---|
| koai:ModelDerivation | 파생 방식은 Finetune·Distill·Merge 중 하나여야 함 |
| 지표 단위(QUDT IRI) | 지표 단위는 QUDT 단위 IRI여야 함(백분율=unit:PERCENT, 점수·개수=unit:NUM, 0~1 비율=unit:UNITLESS) |

## 5. 기계가독 산출물 및 부속서

이 표준을 따르는 데이터의 기계가독 표현은 다음 부속서로 제공한다(운영요령 제19조의3, 작성지침 6.6). 요소 정의표는 4절 본문이며 부속서가 아니다. 별표(★)는 이 표준의 기술 대상 프로파일에서 필수 산출물이다.

| 부속서 | 산출물 | 구성요소 | 형태 | 제공 파일 | 필수/권장 |
|---|---|---|---|---|---|
| 부속서 A | JSON-LD @context | ② 신태틱 | 병행형(작성지침 6.6 a) | `부속서/부속서A_TTAK.KO-10.1594_context.jsonld` | ★ 필수 |
| 부속서 B | SHACL 형상(값 제약 검증) | ③ 데이터 모델 | 병행형(작성지침 6.6 a) | `부속서/부속서B_TTAK.KO-10.1594_shapes.ttl` | ★ 필수 |
| 부속서 C | QUDT/UCUM 단위 정의 | ③ 데이터 모델 | 병행형(작성지침 6.6 a) | `부속서/부속서C_TTAK.KO-10.1594_units.ttl` | 권장 |
| 부속서 D | PROV-O 출처 그래프 | ④ 출처/계보 | 병행형(작성지침 6.6 a) | `부속서/부속서D_TTAK.KO-10.1594_prov.ttl` | ★ 필수 |
| 부속서 E | Croissant ML 계층(학습·검증·시험 분할) | ⑤ 운영 시맨틱 | 참조형(작성지침 6.6 b) | `부속서/부속서E_TTAK.KO-10.1594_croissant.json` | 권장 |
| 부속서 F | DQV 품질 측도 | ⑥ 품질 측도 | 병행형(작성지침 6.6 a) | `부속서/부속서F_TTAK.KO-10.1594_quality.ttl` | 권장 |
| 부속서 G | ODRL 이용정책 | ⑦ 접근/사용 제약 | 병행형(작성지침 6.6 a) | `부속서/부속서G_TTAK.KO-10.1594_policy.jsonld` | 권장 |

**형태.** 병행형 부속서는 부속서에 전문을 수록하고 같은 내용을 파일로도 제공한다. **수록본이 정본**이며 파일은 기계가 직접 처리하기 위한 것이다. 참조형 부속서는 규범적 참조 명세를 두고 실물은 외부 저장소에 두되, **협회 보관본이 정본**이다. 어느 형태이든 파일 자체에 이용조건을 표시했다(5.1).

### 5.1 산출물의 이용조건

이 표준이 제공하는 모든 기계가독 산출물의 이용조건은 **CC BY 4.0**(https://creativecommons.org/licenses/by/4.0/)이다. Turtle 파일은 머리말 주석과 `<> dcterms:license` 트리플로, JSON-LD 파일은 최상위 `$comment` 키와 `http://purl.org/dc/terms/license` 키로 파일 안에 표시했다. 이는 **산출물 자체**의 이용조건이며, 이 표준을 따라 쌓이는 데이터의 이용조건(부속서 G ODRL 이용정책)과는 별개다.

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
| koai | `https://std.tta.or.kr/ns/koai#` |
| dct | `http://purl.org/dc/terms/` |
| dcat | `http://www.w3.org/ns/dcat#` |
| skos | `http://www.w3.org/2004/02/skos/core#` |
| schema | `https://schema.org/` |
| prov | `http://www.w3.org/ns/prov#` |
| qudt | `http://qudt.org/schema/qudt/` |
| xsd | `http://www.w3.org/2001/XMLSchema#` |

### A.3 수록본 (병행형 · 정본)

파일 `부속서/부속서A_TTAK.KO-10.1594_context.jsonld`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
{
  "$comment": "TTAK.KO-10.1594 부속서 A — JSON-LD @context (본 부속서는 표준 내용의 일부임). 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/. 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다(운영요령 제19조의3제2항). 근거: 운영요령 제19조의3제7항, 작성지침 6.6.",
  "http://purl.org/dc/terms/license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "@context": {
    "@version": 1.1,
    "koai": "https://std.tta.or.kr/ns/koai#",
    "dct": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "https://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "AIModel": "koai:AIModel",
    "Dataset": "dcat:Dataset",
    "Task": "koai:Task",
    "Metric": "koai:Metric",
    "Parameter": "koai:Parameter",
    "HyperParameter": "koai:HyperParameter",
    "ModelDerivation": "koai:ModelDerivation",
    "Document": "koai:Document",

    "identifier": "dct:identifier",
    "modelName": "koai:modelName",
    "description": "dct:description",
    "modelArchitecture": "koai:modelArchitecture",
    "framework": "koai:framework",
    "softwareVersion": "schema:softwareVersion",
    "releaseDate": { "@id": "dct:issued", "@type": "xsd:dateTime" },
    "license": { "@id": "dct:license", "@type": "@id" },
    "organization": "koai:organization",
    "modelSize": "koai:modelSize",
    "hasTask": { "@id": "koai:hasTask", "@type": "@id" },
    "hasDocument": { "@id": "koai:hasDocument", "@type": "@id" },

    "TrainingSet": { "@id": "koai:TrainingSet", "@type": "@id" },
    "ValidationSet": { "@id": "koai:ValidationSet", "@type": "@id" },
    "TestSet": { "@id": "koai:TestSet", "@type": "@id" },
    "trainingData": { "@id": "koai:trainingData", "@type": "@id" },
    "hasEvaluationMetric": { "@id": "koai:hasEvaluationMetric", "@type": "@id" },
    "hasTrainingProcess": { "@id": "koai:hasTrainingProcess", "@type": "@id" },
    "hasDerivativeRelation": { "@id": "koai:hasDerivativeRelation", "@type": "@id" },
    "derivativeModel": { "@id": "koai:derivativeModel", "@type": "@id" },
    "derivativeMethod": "koai:derivativeMethod",
    "wasDerivedFrom": { "@id": "prov:wasDerivedFrom", "@type": "@id" },

    "taskCategory": { "@id": "koai:taskCategory", "@type": "@vocab" },
    "metricName": "koai:metricName",
    "hasFormula": "koai:hasFormula",

    "parameterName": "koai:parameterName",
    "parameterValue": "koai:parameterValue",
    "parameterType": "koai:parameterType",
    "usedForPhase": "koai:usedForPhase",
    "tunable": { "@id": "koai:tunable", "@type": "xsd:boolean" },
    "defaultValue": "koai:defaultValue",
    "recommendedRange": "koai:recommendedRange",

    "unit": { "@id": "qudt:unit", "@type": "@vocab" },
    "unitCode": { "@id": "qudt:ucumCode", "@type": "qudt:UCUMcs" },
    "metricUnit": { "@id": "qudt:unit", "@type": "@vocab" },
    "metricUnitCode": { "@id": "qudt:ucumCode", "@type": "qudt:UCUMcs" },

    "distribution": { "@id": "dcat:distribution", "@type": "@id" },
    "keyword": "dcat:keyword",
    "theme": { "@id": "dcat:theme", "@type": "@id" },
    "created": { "@id": "dct:created", "@type": "xsd:dateTime" },
    "modified": { "@id": "dct:modified", "@type": "xsd:dateTime" },
    "accessRights": "dcat:accessRights"
  },
  "_meta": {
    "standard": "TTAK.KO-10.1594",
    "title": "AI 모델의 학습 데이터세트 관리와 상호운용성 지원을 위한 메타데이터",
    "profile": "③ AI 데이터세트",
    "note": "koai 접두어는 본 표준의 자체 온톨로지 네임스페이스(발간 시 확정). 기존 클래스·속성명을 @context 키로 두고 IRI만 매핑하는 최소 전환. split(TrainingSet/ValidationSet/TestSet)·feature/label은 L3에서 Croissant 계층으로 별도 선언 권장.",
    "unitNote": "원 표준이 자유 텍스트로 둔 단위 두 곳(<표 6-5> Parameter.unit 예시 '%,sec,tokens' / <표 6-7> Metric.metricUnit 예시 '비율,%,점수')을 qudt:unit(QUDT 단위 IRI, 규범)으로 승격하고, 이 @context를 해석하지 않는 소비자를 위해 unitCode·metricUnitCode(qudt:ucumCode)를 함께 뒀다. 주의: 'sec'의 UCUM 정규 코드는 's'다. 'tokens'·'점수'는 단위가 아니라 차원 없는 개수이므로 unit:NUM에 UCUM 주석('{tokens}','{score}')을 결합한다 — UCUM 명세상 주석은 unity와 동등하며 적합 파서는 폐기하므로, 세는 대상은 parameterName·metricName이 지시한다. 단위별 IRI·UCUM 코드 대응과 출처 구분은 부속서_units/TTAK.KO-10.1594_units.ttl 참조."
  }
}
```

### A.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서A_TTAK.KO-10.1594_context.jsonld` |
| 형식 | JSON-LD |
| 무결성 확인 값 | `sha256:d233bb9987443bf3011a9b5ff349d0061222548ae46618d94b7f609ce57b55fe` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 B SHACL 형상(값 제약 검증)

**(본 부속서는 표준 내용의 일부임)**

### B.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ③ 데이터 모델의 증빙이다.

### B.2 설계

4절 요소 정의표의 필수 여부·다중성·값 영역을 SHACL 형상으로 옮긴 것이다. 필수 여부와 다중성은 `sh:minCount`·`sh:maxCount`로, 값 범위는 `sh:minInclusive`·`sh:maxInclusive`로, 허용값(코드)은 `sh:in`으로, 길이·형식은 `sh:pattern`·`sh:minLength`·`sh:maxLength`로, 단위는 `sh:hasValue` 또는 `sh:in`으로 대응한다. 형상 전체에 걸리는 규칙(4.6)은 `sh:or`·`sh:closed`·`sh:targetNode`로 표현한다. 요소 정의표를 고치면 이 형상을 다시 생성한다.

### B.3 수록본 (병행형 · 정본)

파일 `부속서/부속서B_TTAK.KO-10.1594_shapes.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1594 부속서 B — SHACL 형상(값 제약 검증)  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# SHACL 검증 스키마 — TTAK.KO-10.1594
# 재생성: 요소 정의표(원천)의 M(필수)/R/O·카디널리티로 minCount/maxCount 구동.
# 구조·열거(sh:in)·데이터타입·값범위 메시지는 보존.

@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dcam: <http://purl.org/dc/dcam/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcmitype: <http://purl.org/dc/dcmitype/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
@prefix koai: <https://std.tta.or.kr/ns/koai#> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix org: <http://www.w3.org/ns/org#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qb: <http://purl.org/linked-data/cube#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix vann: <http://purl.org/vocab/vann/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix wgs: <https://www.w3.org/2003/01/geo/wgs84_pos#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

koai:AIModelShape a sh:NodeShape ;
  sh:targetClass koai:AIModel ;
  sh:property [ sh:path dct:identifier ; sh:name "식별자" ; sh:minCount 1 ; sh:maxCount 1 ; sh:nodeKind sh:IRI ] ;
  sh:property [ sh:path dct:issued ; sh:name "공개일" ; sh:maxCount 1 ; sh:datatype xsd:dateTime ] ;
  sh:property [ sh:path dct:license ; sh:name "라이선스" ; sh:minCount 1 ; sh:maxCount 1 ; sh:nodeKind sh:IRI ] ;
  sh:property [ sh:path koai:framework ; sh:name "프레임워크" ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:hasDocument ; sh:name "모델카드" ; sh:nodeKind sh:IRI ] ;
  sh:property [ sh:path koai:hasTrainingProcess ; sh:name "학습 프로세스" ; sh:maxCount 1 ; sh:nodeKind sh:IRI ] ;
  sh:property [ sh:path koai:modelArchitecture ; sh:name "아키텍처" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:modelName ; sh:name "모델명" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:organization ; sh:name "개발기관" ; sh:maxCount 1 ] ;
  sh:property [ sh:path schema:softwareVersion ; sh:name "버전" ; sh:maxCount 1 ] .

koai:DatasetShape a sh:NodeShape ;
  sh:targetClass dcat:Dataset ;
  sh:property [ sh:path dct:identifier ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path dct:title ; sh:minCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:dataType ; sh:name "데이터 형태" ] .

koai:HyperParameterShape a sh:NodeShape ;
  sh:targetClass koai:HyperParameter ;
  sh:property [ sh:path koai:tunable ; sh:name "조정 가능 여부" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:boolean ] ;
  sh:property [ sh:path koai:usedForPhase ; sh:name "사용 목적" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] .

koai:MetricShape a sh:NodeShape ;
  sh:targetClass koai:Metric ;
  sh:property [ sh:path koai:metricName ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path koai:preferredDirection ; sh:in ( "maximize" "minimize" ) ] ;
  sh:property [ sh:path qudt:unit ; sh:name "지표 단위(QUDT IRI)" ; sh:maxCount 1 ; sh:nodeKind sh:IRI ; sh:in ( <http://qudt.org/vocab/unit/PERCENT> <http://qudt.org/vocab/unit/NUM> <http://qudt.org/vocab/unit/UNITLESS> ) ; sh:message "지표 단위는 QUDT 단위 IRI여야 함(백분율=unit:PERCENT, 점수·개수=unit:NUM, 0~1 비율=unit:UNITLESS)" ] .

koai:ModelDerivationShape a sh:NodeShape ;
  sh:targetClass koai:ModelDerivation ;
  sh:property [ sh:path koai:derivativeMethod ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( "Finetune" "Distill" "Merge" ) ; sh:message "파생 방식은 Finetune·Distill·Merge 중 하나여야 함" ] ;
  sh:property [ sh:path koai:derivativeModel ; sh:minCount 1 ; sh:maxCount 1 ; sh:nodeKind sh:IRI ] .

koai:ParameterShape a sh:NodeShape ;
  sh:targetClass koai:Parameter ;
  sh:property [ sh:path koai:parameterName ; sh:name "파라미터 이름" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:parameterType ; sh:name "값의 타입" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:parameterValue ; sh:name "파라미터 값" ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path qudt:ucumCode ; sh:name "파라미터 단위(UCUM 코드)" ; sh:maxCount 1 ; sh:datatype qudt:UCUMcs ] ;
  sh:property [ sh:path qudt:unit ; sh:name "파라미터 단위(QUDT IRI)" ; sh:maxCount 1 ; sh:nodeKind sh:IRI ; sh:in ( <http://qudt.org/vocab/unit/PERCENT> <http://qudt.org/vocab/unit/SEC> <http://qudt.org/vocab/unit/NUM> <http://qudt.org/vocab/unit/UNITLESS> ) ; sh:message "파라미터 단위는 QUDT 단위 IRI여야 함('%'=unit:PERCENT, 'sec'=unit:SEC, 'tokens'=unit:NUM+UCUM 주석 {tokens})" ] .
```

### B.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서B_TTAK.KO-10.1594_shapes.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:73f14a6f6f85808e8e673e9d0719efbeeda445ea64b3aea117423857733fa6bc` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 C QUDT/UCUM 단위 정의

**(본 부속서는 표준 내용의 일부임)**

### C.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ③ 데이터 모델의 증빙이다.

### C.2 설계

4.5의 단위 결합을 기계가독 형식으로 둔 것이다. 각 단위를 `qudt:unit`(QUDT 단위 IRI, 규범)과 `qudt:ucumCode`(UCUM 코드, 비-RDF 소비자용)로 함께 기술하며, UCUM 코드는 QUDT 공식 어휘의 값을 그대로 옮겼다. 원 표준이 단위를 복수 허용하는 요소는 허용 단위를 모두 등재하고, (단위, 범위) 짝의 검증은 SHACL 형상이 `sh:or`로 수행한다.

### C.3 수록본 (병행형 · 정본)

파일 `부속서/부속서C_TTAK.KO-10.1594_units.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1594 부속서 C — QUDT/UCUM 단위 정의  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# 단위 매핑 부속서 — TTAK.KO-10.1594 (AI 모델의 학습 데이터세트 관리와 상호운용성 지원을 위한 메타데이터)
# 프로파일 ③ AI 데이터세트 · AI-Ready 구성요소: 데이터 모델(L2) / 시맨틱(L1)
#
# [해결하는 문제]
#   원 표준은 단위를 두 곳에서 자유 텍스트로 둔다.
#     · <표 6-5> Parameter.unit      (koai, rdfs:Literal, O) — 본문 예시 '%, sec, tokens'
#     · <표 6-7> Metric.metricUnit   (koai, rdfs:Literal, O) — 본문 예시 '비율, %, 점수'
#   (분석카드 A축 '단위 표기 모호성'은 Parameter.unit만 지적했으나 metricUnit도 같은 결함이다.)
#   비표준 문자열이라 기계 환산·정규화가 불가능하다. 같은 '%'라도 문자열 비교밖에 못 한다.
#
# [해결 방식 — 1530과 동일한 두 경로]
#   1) RDF/그래프 경로 : qudt:unit 으로 QUDT 단위 IRI를 가리킨다 (규범).
#   2) 비-RDF 경로     : qudt:ucumCode 로 UCUM 코드 문자열을 싣는다.
#
# [값의 출처 — 두 종류를 구분해 표기한다]
#   (a) QUDT 전기 : qudt:ucumCode 를 QUDT 공식 vocab에서 그대로 옮긴 값 (2026-07 확인).
#   (b) 로컬 조성 : UCUM 명세의 주석(annotation) 문법으로 이 표준이 조성한 값.
#       UCUM은 중괄호 { } 안에 임의 문자열을 주석으로 허용하며, 선행 심볼이 없으면 단위 1(unity)을
#       뜻한다. 화학·생명과학의 관행('RBC', 'CFU', 'mL(total)')을 수용하기 위한 장치다.
#       주의: UCUM 명세상 주석은 의미론적으로 무의미하며(unity와 동등), 적합 파서는 주석을 폐기한다.
#       즉 '{tokens}'는 "차원 없는 개수"까지만 기계에 전달하고 'tokens'라는 말 자체는 라벨로 남는다.
#
# [모델링 한계 — 개정 시 검토 필요]
#   'tokens'·'점수'는 엄밀히 말해 단위가 아니라 '무엇을 세는가'(quantity kind)에 가깝다.
#   단위는 unit:NUM(차원 없는 개수)으로 두고, 세는 대상은 parameterName·metricName이 지시하도록 한다.
#   QUDT는 이런 도메인 개수 개념에 IRI를 주지 않는다 — UCUM 주석이 현재 유일한 표준 표기다.
#   이것이 이 표준에서 QUDT 단독으로 가지 않고 UCUM을 함께 두는 결정적 근거다.

@prefix koai: <https://std.tta.or.kr/ns/koai#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dcterms:license <https://creativecommons.org/licenses/by/4.0/> .

koai:UnitScheme a skos:ConceptScheme ;
  skos:prefLabel "TTAK.KO-10.1594 파라미터·지표 단위"@ko ;
  rdfs:comment "표 6-5 Parameter.unit 및 표 6-7 Metric.metricUnit이 예시한 자유 텍스트 단위를 QUDT 단위 IRI 및 UCUM 코드에 결합한 목록."@ko .

# ── (a) QUDT 전기 — 공식 ucumCode를 그대로 옮김 ──────────────────────────────

# 백분율 — Parameter.unit '%' · Metric.metricUnit '%'
koai:unit-percent a skos:Concept ; skos:inScheme koai:UnitScheme ;
  skos:prefLabel "%"@ko ;
  skos:altLabel "비율"@ko ;
  rdfs:comment "원문 표기: '%'(표 6-5·표 6-7). ucumCode는 QUDT 공식값."@ko ;
  qudt:unit unit:PERCENT ; qudt:ucumCode "%"^^qudt:UCUMcs .

# 초 — Parameter.unit 'sec'
koai:unit-second a skos:Concept ; skos:inScheme koai:UnitScheme ;
  skos:prefLabel "sec"@ko ;
  rdfs:comment "원문 표기: 'sec'(표 6-5). UCUM 정규 코드는 's'이므로 'sec'을 그대로 쓰면 안 된다. ucumCode는 QUDT 공식값."@ko ;
  qudt:unit unit:SEC ; qudt:ucumCode "s"^^qudt:UCUMcs .

# 개수(일반) — 세는 대상이 지정되지 않은 경우
koai:unit-count a skos:Concept ; skos:inScheme koai:UnitScheme ;
  skos:prefLabel "개수"@ko ;
  rdfs:comment "차원 없는 개수. QUDT qudt:CountingUnit. ucumCode '{#}'는 QUDT 공식값."@ko ;
  qudt:unit unit:NUM ; qudt:ucumCode "{#}"^^qudt:UCUMcs .

# ── (b) 로컬 조성 — UCUM 주석 문법으로 이 표준이 조성 ─────────────────────────

# 토큰 수 — Parameter.unit 'tokens'
koai:unit-token a skos:Concept ; skos:inScheme koai:UnitScheme ;
  skos:prefLabel "tokens"@ko ;
  skos:broader koai:unit-count ;
  rdfs:comment "원문 표기: 'tokens'(표 6-5 예시). 단위가 아니라 차원 없는 개수이며 세는 대상은 parameterName이 지시한다. ucumCode '{tokens}'는 QUDT 전기가 아니라 UCUM 주석 문법으로 조성한 값이며, UCUM 명세상 주석은 unity와 동등하다."@ko ;
  qudt:unit unit:NUM ; qudt:ucumCode "{tokens}"^^qudt:UCUMcs .

# 점수 — Metric.metricUnit '점수'
koai:unit-score a skos:Concept ; skos:inScheme koai:UnitScheme ;
  skos:prefLabel "점수"@ko ;
  skos:broader koai:unit-count ;
  rdfs:comment "원문 표기: '점수'(표 6-7 예시). 차원 없는 값이며 척도는 metricName·hasFormula가 지시한다. ucumCode '{score}'는 UCUM 주석 문법으로 조성한 값이다."@ko ;
  qudt:unit unit:NUM ; qudt:ucumCode "{score}"^^qudt:UCUMcs .

# ── 미해결 ───────────────────────────────────────────────────────────────────
# Metric.metricUnit '비율'은 0~1 비율과 백분율 중 무엇인지 원문이 확정하지 않는다.
# 위 koai:unit-percent 에 altLabel '비율'로 잠정 결합했으나, 개정 시 표 6-7에서
# 척도를 명시해 unit:PERCENT(백분율)와 unit:UNITLESS(0~1 비율)를 분리해야 한다.
# 참고: QUDT는 unit:UNITLESS 에 ucumCode를 공표하지 않는다(UCUM의 unity는 '1').
```

### C.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서C_TTAK.KO-10.1594_units.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:1d1b88767dcf34dea7d5f026a23b80dc1de446f998915a3505c2ecdf006007bb` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 D PROV-O 출처 그래프

**(본 부속서는 표준 내용의 일부임)**

### D.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ④ 출처/계보의 증빙이다.

### D.2 설계

데이터가 누구에 의해 어떤 활동으로 생성·파생됐는지를 PROV-O의 세 축 — 엔티티(데이터·산출물)·활동(생성·처리)·주체(사람·기관) — 과 계보 관계로 형식화한다. 이 부속서는 그 설계를 따른 **예시 인스턴스**이며, 표의 예시 값(기관·데이터세트 이름)은 표준이 특정 대상을 규정하는 것이 아니다. 요소를 참조할 때는 <표 4-2>의 IRI를 쓴다.

| PROV-O 구조 | 이 표준에서의 대응 | 예시 (부속서 D) |
|---|---|---|
| 엔티티 (prov:Entity) | 데이터셋·파일 등 산출물 | KoBERT-base, 감성분석 학습 데이터세트 v1, KoBERT-sentiment |
| 활동 (prov:Activity) | 데이터 생성·처리 활동 | 파인튜닝 학습 |
| 주체 (prov:Agent) | 생성자·발행처·지원기관 | 국립군산대학교 AI연구실 |
| 계보 관계 | 위 세 축을 잇는 관계 | 생성(wasGeneratedBy) · 귀속(wasAttributedTo) · 파생(wasDerivedFrom) · 연관(wasAssociatedWith) · 사용(used) |

### D.3 수록본 (병행형 · 정본)

파일 `부속서/부속서D_TTAK.KO-10.1594_prov.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1594 부속서 D — PROV-O 출처 그래프  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# PROV-O 계보 예시 — TTAK.KO-10.1594 (AI 모델 파생 계보, 출처/계보 L2)
# koai:ModelDerivation(원본→파생)을 PROV-O로 형식화: 학습 활동이 원본 모델·데이터세트를 사용해 파생 모델을 생성.
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix koai: <https://std.tta.or.kr/ns/koai#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/ai/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

ex:base-model a prov:Entity, koai:AIModel ;
  dct:title "KoBERT-base" ;
  dct:license <https://spdx.org/licenses/Apache-2.0> .

ex:train-dataset a prov:Entity, dcat:Dataset, koai:TrainingSet ;
  dct:title "감성분석 학습 데이터세트 v1" ;
  dct:issued "2025-10-01"^^xsd:date .

ex:finetuned-model a prov:Entity, koai:AIModel ;
  dct:title "KoBERT-sentiment" ;
  koai:derivativeMethod "Finetune" ;
  prov:wasDerivedFrom ex:base-model ;
  prov:wasGeneratedBy ex:training-activity ;
  prov:wasAttributedTo ex:lab ;
  dct:created "2025-11-15T09:00:00"^^xsd:dateTime .

ex:training-activity a prov:Activity, koai:TrainingProcess ;
  dct:description "파인튜닝 학습" ;
  prov:startedAtTime "2025-11-10T00:00:00"^^xsd:dateTime ;
  prov:endedAtTime   "2025-11-15T09:00:00"^^xsd:dateTime ;
  prov:used ex:base-model, ex:train-dataset ;
  prov:wasAssociatedWith ex:lab .

ex:lab a prov:Agent, prov:Organization ;
  dct:title "국립군산대학교 AI연구실" .
```

### D.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서D_TTAK.KO-10.1594_prov.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:4cc6782b4a4ecc9d8ccb1930b8c701b025e4fd1674745b1c8ec5911682ef0b7e` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 E Croissant ML 계층(학습·검증·시험 분할)

**(본 부속서는 표준 내용의 일부임)**

### E.1 규범성

이 부속서가 지정하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ⑤ 운영 시맨틱의 증빙이다.

### E.2 설계

학습·검증·시험 분할과 레코드 구조를 Croissant 1.0의 RecordSet·Field로 형식화한다(별표 10 구성요소 ⑤ 운영 시맨틱). 데이터세트 수준에서 split과 feature/label 역할을 한 번 선언하여 ML 도구가 바로 읽게 한다.

| RecordSet (부속서 E) | 필드 |
|---|---|
| splits | name · url |
| examples | split · feature · label |

### E.3 산출물 명세 (참조형)

Croissant 규격은 MLCommons가 표준 문서와 다른 주기로 개정하고, 이 산출물은 데이터세트 배포 파일을 인용하여 단일 파일로 완결되지 아니하므로 참조형으로 둔다(운영요령 제19조의3제3항, 작성지침 6.6 b).

| 항목 | 기재 |
|---|---|
| 산출물 이름 | Croissant ML 계층(학습·검증·시험 분할) |
| 형식 | JSON-LD (Croissant 1.0) |
| 판·버전 | 1.0.0 |
| 무결성 확인 값 | `sha256:f5cb6951aa7dfdaff8662602958ebbfa552a37fd443f8e60724d620a9b60ceac` |
| 이용조건 | CC BY 4.0 — 파일 최상위 `$comment` 키와 `http://purl.org/dc/terms/license` 키에 표시 |

### E.4 소재

| 구분 | 위치 |
|---|---|
| **협회 보관본 (정본)** | 협회 표준 보관소 · 상정 시 제출본 `부속서/부속서E_TTAK.KO-10.1594_croissant.json`을 보관본으로 등록 |
| 외부 공개본 | `https://github.com/<제안기관-저장소>/TTAK.KO-10.1594-ai-ready/blob/v1.0.0/부속서E_TTAK.KO-10.1594_croissant.json` (예시 URL — 실제 공개 시 확정) |

> 보관본과 외부 공개본의 내용이 다른 경우에는 **보관본에 따른다**(운영요령 제19조의3제6항).

### E.5 구성 파일

| No. | 파일명 | 역할 | 무결성 확인 값 |
|---|---|---|---|
| 1 | `부속서E_TTAK.KO-10.1594_croissant.json` | **진입점** (단일 파일) | `sha256:f5cb6951aa7dfdaff8662602958ebbfa552a37fd443f8e60724d620a9b60ceac` |

단일 파일이므로 일괄 내려받기 경로는 두지 아니한다. 파일이 인용하는 데이터세트 배포 파일(`contentUrl`)은 데이터세트 측 자원이며 이 산출물의 구성 파일이 아니다.

### E.6 인용 어휘

| 어휘명 | 네임스페이스 IRI | 이용조건 | 사용 방식 |
|---|---|---|---|
| Croissant ML Metadata 1.0 | `http://mlcommons.org/croissant/` | Apache 2.0 | IRI로 가리킴 |
| schema.org | `https://schema.org/` | CC BY-SA 3.0 | IRI로 가리킴 |
| DCMI Metadata Terms | `http://purl.org/dc/terms/` | CC BY 4.0 | IRI로 가리킴 |

본문 2절의 인용 표준과 일치한다. 보관본 사본의 전문은 참고로 아래에 둔다(규범은 보관본이다).

```
{
  "$comment": "TTAK.KO-10.1594 부속서 E — Croissant ML 계층(학습·검증·시험 분할) (본 부속서는 표준 내용의 일부임). 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/. 협회 보관본(정본)과 외부 공개본이 다를 경우 보관본에 따른다(운영요령 제19조의3제6항). 근거: 운영요령 제19조의3제7항, 작성지침 6.6.",
  "http://purl.org/dc/terms/license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "@context": {
    "@language": "ko",
    "@vocab": "https://schema.org/",
    "cr": "http://mlcommons.org/croissant/",
    "dct": "http://purl.org/dc/terms/",
    "sc": "https://schema.org/",
    "conformsTo": "dct:conformsTo",
    "data": { "@id": "cr:data", "@type": "@json" },
    "dataType": { "@id": "cr:dataType", "@type": "@vocab" },
    "field": "cr:field",
    "fileObject": "cr:fileObject",
    "fileSet": "cr:fileSet",
    "format": "cr:format",
    "includes": "cr:includes",
    "jsonPath": "cr:jsonPath",
    "key": "cr:key",
    "recordSet": "cr:recordSet",
    "references": "cr:references",
    "source": "cr:source",
    "column": "cr:column"
  },
  "@type": "sc:Dataset",
  "conformsTo": "http://mlcommons.org/croissant/1.0",
  "dct:conformsTo": "TTAK.KO-10.1594",
  "name": "example_ai_training_dataset",
  "description": "TTAK.KO-10.1594의 학습 데이터세트(TrainingSet/ValidationSet/TestSet)를 Croissant로 표현한 운영 시맨틱(L3) 예시. 데이터세트 수준에서 split과 feature/label 역할을 1회 선언한다.",
  "license": "https://spdx.org/licenses/CC-BY-4.0",
  "url": "https://example.org/ai-model/dataset",
  "version": "1.0.0",
  "citeAs": "TTAK.KO-10.1594, AI 모델의 학습 데이터세트 관리와 상호운용성 지원을 위한 메타데이터",
  "distribution": [
    {
      "@type": "cr:FileObject",
      "@id": "data.parquet",
      "name": "data.parquet",
      "contentUrl": "https://example.org/ai-model/data.parquet",
      "encodingFormat": "application/x-parquet",
      "sha256": "0000000000000000000000000000000000000000000000000000000000000000"
    }
  ],
  "recordSet": [
    {
      "@type": "cr:RecordSet",
      "@id": "splits",
      "name": "splits",
      "description": "koai:TrainingSet/ValidationSet/TestSet ↔ Croissant split",
      "dataType": "cr:Split",
      "key": { "@id": "splits/name" },
      "field": [
        { "@type": "cr:Field", "@id": "splits/name", "name": "name", "dataType": "sc:Text" },
        { "@type": "cr:Field", "@id": "splits/url",  "name": "url",  "dataType": "sc:URL" }
      ],
      "data": [
        { "splits/name": "train",      "splits/url": "cr:TrainingSplit" },
        { "splits/name": "validation", "splits/url": "cr:ValidationSplit" },
        { "splits/name": "test",       "splits/url": "cr:TestSplit" }
      ]
    },
    {
      "@type": "cr:RecordSet",
      "@id": "examples",
      "name": "examples",
      "description": "각 레코드의 feature/label 역할과 소속 split을 선언.",
      "field": [
        {
          "@type": "cr:Field", "@id": "examples/split", "name": "split",
          "description": "이 레코드가 속한 split(train/validation/test)",
          "dataType": "sc:Text",
          "references": { "field": { "@id": "splits/name" } },
          "source": { "fileObject": { "@id": "data.parquet" }, "extract": { "column": "split" } }
        },
        {
          "@type": "cr:Field", "@id": "examples/feature", "name": "feature",
          "description": "입력 특성(feature) — AI 모델 입력",
          "dataType": "sc:Text",
          "source": { "fileObject": { "@id": "data.parquet" }, "extract": { "column": "text" } }
        },
        {
          "@type": "cr:Field", "@id": "examples/label", "name": "label",
          "description": "레이블(label) — 지도학습 정답",
          "dataType": "sc:Integer",
          "source": { "fileObject": { "@id": "data.parquet" }, "extract": { "column": "label" } }
        }
      ]
    }
  ]
}
```

## 부속서 F DQV 품질 측도

**(본 부속서는 표준 내용의 일부임)**

### F.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ⑥ 품질 측도의 증빙이다.

### F.2 설계

품질을 `dqv:QualityMeasurement`로 형식화하고, 각 측정을 품질 차원(ISO/IEC 5259-2 정렬)에 연결한다. 차원은 이름과 번호로 가리키기만 하고 정의문을 옮겨 적지 아니한다. 예시 측정값은 부속서의 예시 데이터세트 측정치이며 표준이 특정 수치를 규정하지 않는다.

| 품질 차원 (isMeasurementOf) | 예시 측정값 (부속서 F) | 설명 |
|---|---|---|
| syntacticAccuracyRate | 0.992 | 레이블 정확도(참값 대비) |
| completenessRate | 0.998 | 필수 특성·레이블 결측 비율의 역수 |
| diversityScore | 0.8 | 대상 도메인 분포 대비 대표성 |

### F.3 수록본 (병행형 · 정본)

파일 `부속서/부속서F_TTAK.KO-10.1594_quality.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1594 부속서 F — DQV 품질 측도  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# DQV 품질 프로파일 — TTAK.KO-10.1594 (AI 모델 학습 데이터세트, 품질 L3)
# 현재 품질=1(Metric은 '모델 성능지표'이고 데이터세트 자체 품질 부재). 데이터세트 품질을 ISO/IEC 5259-2로 신설.
@prefix dqv:     <http://www.w3.org/ns/dqv#> .
@prefix dcat:    <http://www.w3.org/ns/dcat#> .
@prefix dct:     <http://purl.org/dc/terms/> .
@prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
@prefix iso5259: <https://std.tta.or.kr/ns/iso5259-2#> .
@prefix ex:      <https://example.org/ai/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

ex:train-dataset a dcat:Dataset ;
  dct:title "감성분석 학습 데이터세트 v1" ;
  dct:conformsTo "TTAK.KO-10.1594" ;
  dqv:hasQualityMeasurement ex:q-accuracy, ex:q-completeness, ex:q-representativeness .

ex:q-accuracy a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:syntacticAccuracyRate ;
  dqv:computedOn ex:train-dataset ; dqv:value "0.992"^^xsd:double ;
  dct:description "레이블 정확도(참값 대비)" .

ex:q-completeness a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:completenessRate ;
  dqv:computedOn ex:train-dataset ; dqv:value "0.998"^^xsd:double ;
  dct:description "필수 특성·레이블 결측 비율의 역수" .

ex:q-representativeness a dqv:QualityMeasurement ;
  dqv:isMeasurementOf iso5259:diversityScore ;
  dqv:inDimension iso5259:representativeness ;
  dqv:computedOn ex:train-dataset ; dqv:value "0.80"^^xsd:double ;
  dct:description "대상 도메인 분포 대비 대표성" .
```

### F.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서F_TTAK.KO-10.1594_quality.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:71d35f22610bae6b371ac3fcc136f41c3e80705e237f2f8d8f7b0abf69cd54e8` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 G ODRL 이용정책

**(본 부속서는 표준 내용의 일부임)**

### G.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ⑦ 접근/사용 제약의 증빙이다.

### G.2 설계

이 표준을 따라 쌓이는 **데이터**의 이용조건을 ODRL 2.2 정책으로 형식화한다(별표 10 구성요소 ⑦). 허가(permission)·금지(prohibition)·의무(duty)의 세 규칙으로 나누고, 이용 목적은 DUO 식별자로 적어 기계가 대조하게 한다. 산출물 파일 자체의 이용조건(5.1)과는 별개다.

| 유형 | 행위(action) | 적용 목적·조건 | 의무(duty) |
|---|---|---|---|
| 허가 | 이용·복제·배포·수정 | 조건 없음(전체 적용) | 출처 표시 |
| 금지 | 집계 | 비상업적 이용만(NCU) — gated 배포 시 적용 [DUO_0000046] | — |

### G.3 수록본 (병행형 · 정본)

파일 `부속서/부속서G_TTAK.KO-10.1594_policy.jsonld`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
{
  "$comment": "TTAK.KO-10.1594 부속서 G — ODRL 이용정책 (본 부속서는 표준 내용의 일부임). 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/. 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다(운영요령 제19조의3제2항). 근거: 운영요령 제19조의3제7항, 작성지침 6.6.",
  "http://purl.org/dc/terms/license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    { "duo": "http://purl.obolibrary.org/obo/", "dct": "http://purl.org/dc/terms/" }
  ],
  "@type": "Offer",
  "uid": "https://std.tta.or.kr/policy/1594/model-offer",
  "dct:conformsTo": "TTAK.KO-10.1594",
  "dct:description": "AI 모델 이용정책 예시(접근/제약 L3). dct:license(SPDX)에 더해 접근수준(public/gated/private)과 이용조건을 ODRL로 형식화.",
  "profile": "https://std.tta.or.kr/profile/ai-dataset",
  "permission": [
    {
      "target": "https://example.org/ai/model/kobert-sentiment",
      "assigner": "https://example.org/lab",
      "action": [ "use", "reproduce", "distribute", "modify" ],
      "duty": [
        { "action": "attribute",
          "constraint": [ { "leftOperand": "source", "operator": "eq",
                            "rightOperand": "https://spdx.org/licenses/Apache-2.0" } ] }
      ]
    }
  ],
  "prohibition": [
    {
      "target": "https://example.org/ai/model/kobert-sentiment",
      "action": [ "aggregate" ],
      "constraint": [
        { "leftOperand": "purpose", "operator": "eq",
          "rightOperand": { "@id": "duo:DUO_0000046" },
          "rdfs:comment": "비상업적 이용만(NCU) — gated 배포 시 적용" }
      ]
    }
  ],
  "_meta": {
    "license": "Apache-2.0 (permissive)",
    "accessLevel": "koai:AccessService = public | gated | private",
    "note": "허용형 라이선스라 permission 중심. gated/private는 recipient·purpose 제약으로 표현. DUO_0000046=non-commercial use only."
  }
}
```

### G.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서G_TTAK.KO-10.1594_policy.jsonld` |
| 형식 | JSON-LD |
| 무결성 확인 값 | `sha256:8b62ab8e6636ce62a8e6bde3637d89dcc559aa5d453dccc85f2222acb893dca7` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부록 (자유 작성) 참조구현 안내

이 표준의 부속서 B의 SHACL 형상으로 데이터 인스턴스를 검증하는 스크립트를 다음 위치에 공개한다.

| 항목 | 기재 |
|---|---|
| 위치 | `https://github.com/<제안기관-저장소>/TTAK.KO-10.1594-ai-ready/tree/main/tools` (예시 URL — 실제 공개 시 확정) |
| 언어·런타임 | Python 3.11 · pySHACL |
| 라이선스 | MIT |

**참조구현은 표준의 일부가 아니며, 협회는 그 내용에 대하여 보증하지 아니한다**(운영요령 제19조의3제8항). 참조구현의 동작이 부속서와 다를 경우 부속서에 따른다.

## 부록 (자유 작성) 원 표준 대비 교정 사항

원 표준의 현행 진단에서 확인된 정합성 결함(4건 — 규범 @context 부재(신태틱 1등급 원인), 지표 단위 미결합, 하이퍼파라미터 열거값 불일치, 표 표제 오기 등 4건)을 이 개정에서 본문·부속서로 교정했다. 교정 결과는 자가점검표 2부에 적었다.
