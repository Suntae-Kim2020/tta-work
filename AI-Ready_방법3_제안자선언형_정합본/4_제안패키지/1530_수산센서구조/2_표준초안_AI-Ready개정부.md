# TTAK.KO-10.1530 AI-Ready 개정 표준초안(개정부) — 유수식 스마트 수산양식 시스템의 센서 데이터 구조
정보통신단체표준(국문표준) · TTAK.KO-10.1530 · 제정 2024.12.06 · AI-Ready 개정 제안 · 소관 PG426 (스마트 수산) · 에디터 ETRI(한국전자통신연구원)

> 이 초안은 **AI-Ready 개정부 중심**으로 작성되었다. 원 표준의 도메인 본문(적용범위·용어·요소 상세)은 원 표준을 계승·참조하고, AI-Ready 개정으로 새로 추가·강화되는 부분 — 인용 표준 보강(2절), 요소 정의표의 전역 어휘 식별자(4절), 기계가독 부속서(5절·부속서), 참조구현 안내(부록) — 을 실제로 채웠다. 절 번호와 양식은 「정보통신단체표준 작성지침(TTAR-09.0040)」과 그 AI-Ready 개정안(6.5.3·6.5.7·6.6·6.7)을 따른다.

> **작성 주체.** 요소 정의표의 전역 어휘 식별자(IRI) 매핑과 모든 부속서는 **에디터**가 제안 단계의 「기계가독 산출물 선언서」(별지 제11-1호서식)에 따라 작성했다(운영요령 제19조의3제1항, 작성지침 6.5.7). 별도의 공동 에디터(어휘 전문가)를 두지 아니한다. 선언과의 일치는 상정 시 자가점검표(별지 제21-1호서식) 3부에서 확인한다.

## 서문

이 표준은 「유수식 스마트 수산양식 시스템의 센서 데이터 구조」의 개정판이다. 원 표준(제정 2024.12.06)의 적용범위와 데이터 구조를 계승하되, 데이터를 사람과 기계가 함께 읽을 수 있도록 각 데이터 요소의 의미를 전역 어휘 식별자(IRI)에 매핑하고, 그 매핑을 JSON-LD @context로 배포하며, 값 제약·출처·품질·이용조건을 기계가독 부속서로 제공한다. 이로써 이 표준을 따르는 데이터는 별도 해석 없이 상호운용·검증·재이용이 가능해진다.

**AI-Ready 목표 수준** — 기술 대상 프로파일 ② 자기기술형 레코드 (센서 관측 레코드) · 필수 시맨틱 · 신태틱 · 데이터 모델 · 권장 + 출처 (= L2). (근거: 첨부 「기계가독 산출물 선언서」 및 「AI-Ready 자가점검표」)

## 1. 적용범위

이 표준은 「유수식 스마트 수산양식 시스템의 센서 데이터 구조」이 규정하는 데이터의 요소·구조·값 형식을 계승하며(원 표준 1절 참조), 그 데이터 요소를 전역 어휘에 매핑하여 기계가독 형식으로 배포하기 위한 요소 정의·인용 표준·부속서 구성을 규정한다. 원 표준의 도메인 규정은 변경 없이 유지되고, 이 개정은 그 위에 기계가독 계층을 더한다.

## 2. 인용 표준

다음 표준·어휘는 이 표준의 적용에 필수적이며, 본문에서 인용되는 범위에서 이 표준의 일부를 구성한다. 선언서 2에서 선언한 외부 어휘를 **모두** 등재한다(작성지침 6.5.3 · 운영요령 제19조제1항제9호). 종전에 참고 문헌에 두었던 어휘도 요소 의미가 규범적으로 의존하므로 인용 표준으로 올린다.

| 인용 표준 · 어휘 | 발행 주체 | 이 표준에서의 용도(접두어) | 사용 방식 |
|---|---|---|---|
| JSON-LD 1.1 | W3C | 요소↔IRI 매핑의 규범 직렬화(부속서 A) | 직렬화 규격 |
| Semantic Sensor Network (SOSA/SSN) | W3C | sosa: 클래스 2 · 속성 4 / 부속서 A·B·D에서 사용 | IRI로 가리킴 |
| Semantic Sensor Network (SOSA/SSN) | W3C | ssn: 부속서 A에서 사용 | IRI로 가리킴 |
| QUDT Schema | QUDT.org | qudt: ucumCode: 단위 코드 문자열 | IRI로 가리킴 |
| QUDT Units Vocabulary | QUDT.org | unit: 부속서 A·B·C에서 사용 | IRI로 가리킴 |
| DCMI Metadata Terms | DCMI | dct: 식별자·명칭·설치시각 | IRI로 가리킴 |
| GeoSPARQL 1.1 | OGC | geo: 설치 위치 좌표 | IRI로 가리킴 |
| PROV-O: The PROV Ontology | W3C | prov: 부속서 D에서 사용 | IRI로 가리킴 |
| SKOS Simple Knowledge Organization System | W3C | skos: 부속서 C에서 사용 | IRI로 가리킴 |
| Shapes Constraint Language (SHACL) | W3C | sh: 값 검증 언어 — 부속서 B | IRI로 가리킴 |
| FOAF Vocabulary | FOAF Project | foaf: 부속서 D에서 사용 | IRI로 가리킴 |
| XML Schema Part 2: Datatypes | W3C | xsd: 데이터 유형(리터럴) | IRI로 가리킴 |

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

이 절이 AI-Ready 개정의 핵심이며, 모든 기계가독 부속서가 파생되는 원천이다. 원 표준이 정의한 데이터 요소 27개 전체를 작성지침 6.5.7의 요소 정의표로 규정한다(이 표준 필수 M 7개 · 권장 R 6개). 컬럼이 14개로 많으므로 <표 6-5>의 허용에 따라 표를 둘로 나누었다 — <표 4-1>은 값의 형식(요소 이름·표시명·데이터 유형·값 영역·다중성·필수 여부·단위), <표 4-2>는 어휘 바인딩(요소 이름·출처·버전·전역 어휘 식별자·비고)이다.

> **개정부 초안의 범위.** 14개 컬럼 가운데 **정의·기본값·예시**는 원 표준의 요소 상세를 그대로 계승하므로 이 개정부 초안에서는 생략하고, 통합본 작성 시 <표 6-5>에 따라 모두 채운다. 다중성·필수 여부는 소속 객체 기준이다(예: 파라미터 이름은 "파라미터가 있으면 반드시"). '권장'은 원 표준의 R(권장)을 뜻하며 작성지침의 필수 여부 구분(필수·선택·조건부)에서는 선택에 해당하므로 비고에 적었다.

### 4.1 객체(클래스)

요소가 소속되는 객체다. 객체는 값을 갖지 않으므로 다중성·필수 여부는 해당 없음이다.

| 객체 이름 | 표시명 | 출처 | 전역 어휘 식별자(IRI) |
|---|---|---|---|
| `Section` | 수조 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/koai#WaterTank`) |
| `Device` | 센서 | Semantic Sensor Network (SOSA/SSN) | `http://www.w3.org/ns/sosa/Sensor` |
| `Observation` | 관측 | Semantic Sensor Network (SOSA/SSN) | `http://www.w3.org/ns/sosa/Observation` |

### 4.2 요소 — 값의 형식 <표 4-1>

| 요소 이름 | 표시명 | 데이터 유형 | 값 영역 | 다중성 | 필수 여부 | 단위 |
|---|---|---|---|---|---|---|
| `SectionID` | 수조 식별자 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `SectionName` | 수조명 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `FishType` | 어종 | 문자열 | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `FishNum` | 개체 수 | 정수 | 0 이상 | 0..1 | 선택 | 해당 없음 |
| `Area` | 사육 면적 | 실수 | 0 이상 | 0..1 | 선택 | m² |
| `Density` | 사육 밀도 | 실수 | 0 이상 | 0..1 | 선택 | kg/m³ |
| `DeviceID` | 센서 식별자 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `DeviceName` | 센서명 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `ModelName` | 모델명 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `ManufName` | 제조사 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `Type` | 관측 대상 | 코드 | pH · 수온 · 유량 · 용존CO2 · 용존산소 · 염도 · ORP · 전도도 · 탁도 · 수위 (표 6-1) | 1 | 필수 | 해당 없음 |
| `ReptIntrv` | 보고 주기 | 정수 | 제한 없음 | 0..1 | 선택 | s |
| `ValueUnit` | 단위(IRI) | 코드 | unit:PH · DEG_C · L-PER-MIN · MilliGM-PER-L · GM-PER-KiloGM · MilliV · MicroS-PER-CentiM · NTU · M · PPM · PERCENT · PPTH (부속서 C) | 1 | 필수 | 해당 없음 |
| `ValueUnitCode` | 단위 코드(UCUM) | 문자열 | 부속서 C의 UCUM 코드. NTU는 UCUM에 정의가 없어 예외 | 1 | 필수 | 해당 없음 |
| `ValueType` | 값 유형 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `InstallTime` | 설치 시각 | 날짜시간 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `LocX` | 위도 | 문자열 | 제한 없음 | 0..1 | 선택 | ° |
| `LocY` | 경도 | 문자열 | 제한 없음 | 0..1 | 선택 | ° |
| `InstallStatus` | 설치 상태 | 코드 | 코드 목록(부속서 B sh:in) | 0..1 | 선택 | 해당 없음 |
| `DevOperStatus` | 운영 상태 | 코드 | OFF · READY | 0..1 | 선택 | 해당 없음 |
| `SensingTime` | 측정 시각 | 날짜시간 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `Value` | 측정값 | 실수 | 관측대상·단위별 (표 6-1) — pH 0~14 / 수온 0~50℃ / 유량 2~3600 L/min / 용존CO2 mg/L·ppm 0~20, % 0~200 / 용존산소 mg/L 0~50, % 0~200 / 염도 g/kg 5~60, ppt 0~50, ppm 0~50000 / ORP -1000~1400 mV / 전도도 0~200 μS/cm / 탁도 NTU 0~4000, mg/L 0~4500 / 수위 1~20 m | 1 | 필수 | 관측대상별(부속서 C) |
| `ValueState` | 유효성 수준 | 코드 | low · normal · high | 0..1 | 선택 | 해당 없음 |
| `Status` | 결과 품질 | 코드 | 준비 · 정상 · 동작전압이상 · 동작전류이상 · 동작온도이상 · 소모품교체 · 센서교정요망 · 센서점검필요 · 오작동 | 0..1 | 선택 | 해당 없음 |

### 4.3 요소 — 어휘 바인딩 <표 4-2>

전역 어휘 식별자(IRI) 컬럼은 에디터가 선언서 2의 어휘 범위 안에서 작성했다. 자체 정의 요소는 '자체 정의'로 적고 비고에 이 표준의 네임스페이스 IRI를 밝힌다. 직렬화 키(@context의 키)는 요소 이름과 같다.

| 요소 이름 | 출처 | 버전 | 전역 어휘 식별자(IRI) | 비고 |
|---|---|---|---|---|
| `SectionID` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/identifier` | 리터럴 유형 xsd:ID |
| `SectionName` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/title` | 해당 없음 |
| `FishType` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#fishType` |
| `FishNum` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#fishCount` |
| `Area` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#rearingArea` |
| `Density` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#rearingDensity` · 권장 |
| `DeviceID` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/identifier` | 리터럴 유형 xsd:ID |
| `DeviceName` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/title` | 해당 없음 |
| `ModelName` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#modelName` |
| `ManufName` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#manufacturer` |
| `Type` | Semantic Sensor Network (SOSA/SSN) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/sosa/observedProperty` | 해당 없음 |
| `ReptIntrv` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#reportInterval` |
| `ValueUnit` | QUDT Schema | 이번 AI-Ready 개정판 | `http://qudt.org/schema/qudt/unit` | 해당 없음 |
| `ValueUnitCode` | QUDT Schema | 이번 AI-Ready 개정판 | `http://qudt.org/schema/qudt/ucumCode` | 리터럴 유형 qudt:UCUMcs |
| `ValueType` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#valueType` |
| `InstallTime` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/created` | 권장 |
| `LocX` | GeoSPARQL 1.1 | 이번 AI-Ready 개정판 | `http://www.opengis.net/ont/geosparql#lat` | 권장 |
| `LocY` | GeoSPARQL 1.1 | 이번 AI-Ready 개정판 | `http://www.opengis.net/ont/geosparql#long` | 권장 |
| `InstallStatus` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#installStatus` |
| `DevOperStatus` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#operationStatus` |
| `SensingTime` | Semantic Sensor Network (SOSA/SSN) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/sosa/resultTime` | 해당 없음 |
| `Value` | Semantic Sensor Network (SOSA/SSN) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/sosa/hasSimpleResult` | 해당 없음 |
| `ValueState` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/koai#validityLevel` · 권장 |
| `Status` | Semantic Sensor Network (SOSA/SSN) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/sosa/hasResultQuality` | 권장 |

### 4.4 코드·열거값

코드(열거) 유형 요소의 허용값이다. 부속서의 SHACL 형상에서 `sh:in` 제약으로 검증한다.

| 요소 | 허용값 목록 |
|---|---|
| 운용상태(koai:operationStatus) | OFF · READY |
| 값수준(koai:validityLevel) | low · normal · high |
| 센서상태(sosa:hasResultQuality) | 준비 · 정상 · 동작전압이상 · 동작전류이상 · 동작온도이상 · 소모품교체 · 센서교정요망 · 센서점검필요 · 오작동 |

### 4.5 단위

측정값 요소의 단위를 QUDT 단위 IRI(규범)와 UCUM 코드(비-RDF 소비자용)에 함께 결합한다(작성지침 부속서 B.4). 단위 부속서에 같은 내용을 기계가독 형식으로 둔다.

| 단위(표기) | QUDT 단위 IRI | UCUM 코드 | 적용 범위 |
|---|---|---|---|
| pH | `http://qudt.org/vocab/unit/PH` | [pH] | 측정범위 0~14 |
| ℃ | `http://qudt.org/vocab/unit/DEG_C` | Cel | 수온 측정범위 0~50 |
| L/min | `http://qudt.org/vocab/unit/L-PER-MIN` | L.min-1 | 유량 측정범위 2~3600 |
| mg/L | `http://qudt.org/vocab/unit/MilliGM-PER-L` | mg.L-1 | 용존CO2 0~20, 용존산소 0~50 |
| g/kg | `http://qudt.org/vocab/unit/GM-PER-KiloGM` | g.kg-1 | 염도 측정범위 5~60 |
| mV | `http://qudt.org/vocab/unit/MilliV` | mV | ORP 측정범위 -1000~1400 |
| μS/cm | `http://qudt.org/vocab/unit/MicroS-PER-CentiM` | uS.cm-1 | 전도도 측정범위 0~200 |
| NTU | `http://qudt.org/vocab/unit/NTU` | — (미정의) | 탁도 측정범위 0~4000. UCUM에 정의가 없어 QUDT IRI만 사용한다. |
| m | `http://qudt.org/vocab/unit/M` | m | 수위 측정범위 1~20 |

## 5. 기계가독 산출물 및 부속서

이 표준을 따르는 데이터의 기계가독 표현은 다음 부속서로 제공한다(운영요령 제19조의3, 작성지침 6.6). 요소 정의표는 4절 본문이며 부속서가 아니다. 별표(★)는 이 표준의 기술 대상 프로파일에서 필수 산출물이다.

| 부속서 | 산출물 | 구성요소 | 형태 | 제공 파일 | 필수/권장 |
|---|---|---|---|---|---|
| 부속서 A | JSON-LD @context | ② 신태틱 | 병행형(작성지침 6.6 a) | `부속서/부속서A_TTAK.KO-10.1530_context.jsonld` | ★ 필수 |
| 부속서 B | SHACL 형상(값 제약 검증) | ③ 데이터 모델 | 병행형(작성지침 6.6 a) | `부속서/부속서B_TTAK.KO-10.1530_shapes.ttl` | ★ 필수 |
| 부속서 C | QUDT/UCUM 단위 정의 | ③ 데이터 모델 | 병행형(작성지침 6.6 a) | `부속서/부속서C_TTAK.KO-10.1530_units.ttl` | ★ 필수 |
| 부속서 D | PROV-O 출처 그래프 | ④ 출처/계보 | 병행형(작성지침 6.6 a) | `부속서/부속서D_TTAK.KO-10.1530_prov.ttl` | 권장 |

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
| sosa | `http://www.w3.org/ns/sosa/` |
| ssn | `http://www.w3.org/ns/ssn/` |
| qudt | `http://qudt.org/schema/qudt/` |
| unit | `http://qudt.org/vocab/unit/` |
| dct | `http://purl.org/dc/terms/` |
| geo | `http://www.opengis.net/ont/geosparql#` |
| koai | `https://std.tta.or.kr/ns/koai#` |
| xsd | `http://www.w3.org/2001/XMLSchema#` |

### A.3 수록본 (병행형 · 정본)

파일 `부속서/부속서A_TTAK.KO-10.1530_context.jsonld`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
{
  "$comment": "TTAK.KO-10.1530 부속서 A — JSON-LD @context (본 부속서는 표준 내용의 일부임). 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/. 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다(운영요령 제19조의3제2항). 근거: 운영요령 제19조의3제7항, 작성지침 6.6.",
  "http://purl.org/dc/terms/license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "@context": {
    "@version": 1.1,
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn": "http://www.w3.org/ns/ssn/",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "dct": "http://purl.org/dc/terms/",
    "geo": "http://www.opengis.net/ont/geosparql#",
    "koai": "https://std.tta.or.kr/ns/koai#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "Section": "koai:WaterTank",
    "Device": "sosa:Sensor",
    "Observation": "sosa:Observation",

    "SectionID": { "@id": "dct:identifier", "@type": "xsd:ID" },
    "SectionName": "dct:title",
    "FishType": "koai:fishType",
    "FishNum": { "@id": "koai:fishCount", "@type": "xsd:integer" },
    "Area": { "@id": "koai:rearingArea", "@type": "xsd:decimal" },
    "Density": { "@id": "koai:rearingDensity", "@type": "xsd:decimal" },

    "DeviceID": { "@id": "dct:identifier", "@type": "xsd:ID" },
    "DeviceName": "dct:title",
    "ModelName": "koai:modelName",
    "ManufName": "koai:manufacturer",
    "Type": { "@id": "sosa:observedProperty", "@type": "@vocab" },
    "ReptIntrv": { "@id": "koai:reportInterval", "@type": "xsd:short" },
    "ValueUnit": { "@id": "qudt:unit", "@type": "@vocab" },
    "ValueUnitCode": { "@id": "qudt:ucumCode", "@type": "qudt:UCUMcs" },
    "ValueType": "koai:valueType",

    "InstallTime": { "@id": "dct:created", "@type": "xsd:dateTime" },
    "LocX": "geo:lat",
    "LocY": "geo:long",
    "InstallStatus": { "@id": "koai:installStatus", "@type": "@vocab" },
    "DevOperStatus": { "@id": "koai:operationStatus", "@type": "@vocab" },

    "SensingTime": { "@id": "sosa:resultTime", "@type": "xsd:dateTime" },
    "Value": { "@id": "sosa:hasSimpleResult", "@type": "xsd:float" },
    "ValueState": { "@id": "koai:validityLevel", "@type": "@vocab" },
    "Status": { "@id": "sosa:hasResultQuality", "@type": "@vocab" }
  },
  "_meta": {
    "standard": "TTAK.KO-10.1530",
    "title": "유수식 스마트 수산양식 시스템의 센서 데이터 구조",
    "profile": "② 자기기술형 레코드",
    "note": "센서 코드값(Type 0x01~0x0B, ValueUnit)을 SOSA observedProperty·QUDT unit IRI로 승격. 측정범위·enum은 SHACL(sh:minInclusive 등)로 형식화. 매핑 대상 단위: pH·oC(unit:DEG_C)·mg/L(unit:MilliGM-PER-L)·NTU 등.",
    "unitNote": "단위는 두 경로로 표기한다. ValueUnit=qudt:unit(QUDT 단위 IRI, 규범) / ValueUnitCode=qudt:ucumCode(UCUM 코드 문자열). 후자는 이 @context를 해석하지 않는 소비자(센서 게이트웨이·기존 계측 시스템)를 위한 것이다 — 그들에게 'unit:MilliGM-PER-L'은 뜻 없는 문자열이나 'mg.L-1'은 국제 표준 코드이며, UCUM은 문법이라 파싱만으로 차원 계산·단위 변환이 된다. UCUM은 지수 표기이므로 'mg/L'이 아니라 'mg.L-1'이다. 단위별 IRI·UCUM 코드 대응은 부속서_units/TTAK.KO-10.1530_units.ttl 참조. 탁도(NTU)는 UCUM 미정의로 IRI 경로만 가능."
  }
}
```

### A.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서A_TTAK.KO-10.1530_context.jsonld` |
| 형식 | JSON-LD |
| 무결성 확인 값 | `sha256:b302f179d31f3b0886644a7c67b3807b69b772a24d976f804e65911bb13a49ec` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 B SHACL 형상(값 제약 검증)

**(본 부속서는 표준 내용의 일부임)**

### B.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ③ 데이터 모델의 증빙이다.

### B.2 설계

4절 요소 정의표의 필수 여부·다중성·값 영역을 SHACL 형상으로 옮긴 것이다. 필수 여부와 다중성은 `sh:minCount`·`sh:maxCount`로, 값 범위는 `sh:minInclusive`·`sh:maxInclusive`로, 허용값(코드)은 `sh:in`으로, 길이·형식은 `sh:pattern`·`sh:minLength`·`sh:maxLength`로, 단위는 `sh:hasValue` 또는 `sh:in`으로 대응한다. 형상 전체에 걸리는 규칙(4.6)은 `sh:or`·`sh:closed`·`sh:targetNode`로 표현한다. 요소 정의표를 고치면 이 형상을 다시 생성한다.

### B.3 수록본 (병행형 · 정본)

파일 `부속서/부속서B_TTAK.KO-10.1530_shapes.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1530 부속서 B — SHACL 형상(값 제약 검증)  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# SHACL 검증 스키마 — TTAK.KO-10.1530
# 재생성: 요소 정의표(원천)의 M(필수)/R/O·카디널리티로 minCount/maxCount 구동.
# 값 제약(범위·단위)은 원 표준 <표 6-1>에서 옮긴다 — 설계 명세 §4·§5의 → SHACL 매핑 참조.
#
# [단위와 값범위는 한 쌍이다]
#   표 6-1은 센서에 따라 단위를 복수로 허용하며, 허용 범위가 단위마다 다르다
#   (예: 용존CO2 mg/L·ppm 0~20 / % 0~200). 따라서 단위 하나를 골라 고정하지 않고,
#   (단위, 범위) 짝을 sh:or 로 나열해 원 표준이 허용하는 표현을 모두 통과시킨다.
#   단위 IRI·UCUM 코드의 근거는 부속서 C(단위 매핑)를 참조한다.

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

koai:CO2ObsShape a sh:NodeShape ;
  sh:targetClass koai:CO2Observation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 (mg/L · ppm · %)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( unit:MilliGM-PER-L unit:PPM unit:PERCENT ) ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "용존CO2" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ] ;
  sh:or (
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:MilliGM-PER-L ] ; sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 20 ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:PPM ] ;           sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 20 ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:PERCENT ] ;       sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 200 ] ]
  ) ;
  sh:message "용존CO2 — mg/L·ppm은 0~20, %는 0~200 (표 6-1)" .

koai:ConductivityObsShape a sh:NodeShape ;
  sh:targetClass koai:ConductivityObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 μS/cm" ; sh:minCount 1 ; sh:maxCount 1 ; sh:hasValue unit:MicroS-PER-CentiM ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "전도도 0~200 μS/cm" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ; sh:minInclusive 0 ; sh:maxInclusive 200 ; sh:message "전도도는 0~200 μS/cm (표 6-1)" ] .

koai:DOObsShape a sh:NodeShape ;
  sh:targetClass koai:DOObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 (mg/L · %)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( unit:MilliGM-PER-L unit:PERCENT ) ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "용존산소" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ] ;
  sh:or (
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:MilliGM-PER-L ] ; sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 50 ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:PERCENT ] ;       sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 200 ] ]
  ) ;
  sh:message "용존산소 — mg/L은 0~50, %는 0~200 (표 6-1)" .

koai:DeviceShape a sh:NodeShape ;
  sh:targetClass sosa:Sensor ;
  sh:property [ sh:path dct:identifier ; sh:name "디바이스 식별자" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:operationStatus ; sh:name "운용상태" ; sh:maxCount 1 ; sh:in ( "OFF" "READY" ) ] ;
  sh:property [ sh:path koai:reportInterval ; sh:name "센싱주기(분)" ; sh:maxCount 1 ; sh:datatype xsd:short ] ;
  # 표 6-1이 허용하는 단위 전체. mg/L·ppm·%·ppt는 센서에 따라 병용되므로 모두 허용한다.
  sh:property [ sh:path qudt:unit ; sh:name "측정 단위(QUDT IRI)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:nodeKind sh:IRI ; sh:in ( unit:PH unit:DEG_C unit:L-PER-MIN unit:MilliGM-PER-L unit:GM-PER-KiloGM unit:MilliV unit:MicroS-PER-CentiM unit:NTU unit:M unit:PPM unit:PERCENT unit:PPTH ) ] ;
  sh:property [ sh:path qudt:ucumCode ; sh:name "측정 단위(UCUM 코드)" ; sh:maxCount 1 ; sh:datatype qudt:UCUMcs ] .

koai:FlowObsShape a sh:NodeShape ;
  sh:targetClass koai:FlowObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 L/min" ; sh:minCount 1 ; sh:maxCount 1 ; sh:hasValue unit:L-PER-MIN ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "유량 2~3600 L/min" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:integer ; sh:minInclusive 2 ; sh:maxInclusive 3600 ; sh:message "유량은 2~3600 L/min (표 6-1)" ] .

koai:ORPObsShape a sh:NodeShape ;
  sh:targetClass koai:ORPObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 mV" ; sh:minCount 1 ; sh:maxCount 1 ; sh:hasValue unit:MilliV ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "ORP -1000~1400 mV" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ; sh:minInclusive -1000 ; sh:maxInclusive 1400 ; sh:message "ORP는 -1000~1400 mV (표 6-1)" ] .

koai:ObservationShape a sh:NodeShape ;
  sh:targetClass sosa:Observation ;
  sh:property [ sh:path koai:validityLevel ; sh:name "값수준" ; sh:maxCount 1 ; sh:in ( "low" "normal" "high" ) ] ;
  sh:property [ sh:path sosa:hasResultQuality ; sh:name "센서상태" ; sh:maxCount 1 ; sh:in ( "준비" "정상" "동작전압이상" "동작전류이상" "동작온도이상" "소모품교체" "센서교정요망" "센서점검필요" "오작동" ) ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "센싱값" ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path sosa:resultTime ; sh:name "센싱시각" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:dateTime ] ;
  # 값은 단위 없이 오지 못한다. QUDT 단위 IRI(규범)에 더해 UCUM 코드를 함께 싣는다 —
  # @context를 해석하지 않는 소비자(게이트웨이·기존 계측 시스템)는 IRI를 읽지 못하지만
  # UCUM은 문법이라 파싱만으로 차원 계산·단위 변환이 된다(요소 정의표 ValueUnitCode M(1)).
  # 다만 NTU는 UCUM에 정의가 없어 QUDT IRI만 둔다 — 부속서 C가 밝힌 유일한 예외다.
  sh:or (
    [ sh:property [ sh:path qudt:ucumCode ; sh:minCount 1 ; sh:datatype qudt:UCUMcs ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:NTU ] ]
  ) ;
  sh:message "단위 코드(UCUM)를 함께 실어야 한다. UCUM에 정의가 없는 NTU(탁도)만 예외다." .

koai:PHObsShape a sh:NodeShape ;
  sh:targetClass koai:PHObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 pH" ; sh:minCount 1 ; sh:maxCount 1 ; sh:hasValue unit:PH ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "pH 0~14" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ; sh:minInclusive 0 ; sh:maxInclusive 14 ; sh:message "pH는 0~14 (표 6-1)" ] .

koai:SalinityObsShape a sh:NodeShape ;
  sh:targetClass koai:SalinityObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 (g/kg · ppt · ppm)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( unit:GM-PER-KiloGM unit:PPTH unit:PPM ) ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "염도" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ] ;
  sh:or (
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:GM-PER-KiloGM ] ; sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 5 ; sh:maxInclusive 60 ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:PPTH ] ;          sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 50 ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:PPM ] ;           sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 50000 ] ]
  ) ;
  sh:message "염도 — g/kg은 5~60, ppt는 0~50, ppm은 0~50000 (표 6-1)" .

koai:SectionShape a sh:NodeShape ;
  sh:targetClass koai:WaterTank ;
  sh:property [ sh:path dct:identifier ; sh:name "수조 식별자" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:fishCount ; sh:name "사육수량" ; sh:maxCount 1 ; sh:datatype xsd:integer ; sh:minInclusive 0 ; sh:message "사육수량은 0 이상" ] ;
  sh:property [ sh:path koai:fishType ; sh:name "어종" ; sh:datatype xsd:string ] ;
  sh:property [ sh:path koai:rearingArea ; sh:name "사육면적" ; sh:maxCount 1 ; sh:datatype xsd:decimal ; sh:minInclusive 0 ; sh:message "사육면적은 0 이상" ] ;
  sh:property [ sh:path koai:rearingDensity ; sh:name "사육밀도" ; sh:maxCount 1 ; sh:datatype xsd:decimal ; sh:minInclusive 0 ; sh:message "사육밀도는 0 이상" ] .

koai:TurbidityObsShape a sh:NodeShape ;
  sh:targetClass koai:TurbidityObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 (NTU · mg/L)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( unit:NTU unit:MilliGM-PER-L ) ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "탁도" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ] ;
  sh:or (
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:NTU ] ;           sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 4000 ] ]
    [ sh:property [ sh:path qudt:unit ; sh:hasValue unit:MilliGM-PER-L ] ; sh:property [ sh:path sosa:hasSimpleResult ; sh:minInclusive 0 ; sh:maxInclusive 4500 ] ]
  ) ;
  sh:message "탁도 — NTU는 0~4000, mg/L은 0~4500 (표 6-1)" .

koai:WaterLevelObsShape a sh:NodeShape ;
  sh:targetClass koai:WaterLevelObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 m" ; sh:minCount 1 ; sh:maxCount 1 ; sh:hasValue unit:M ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "수위 1~20 m" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ; sh:minInclusive 1 ; sh:maxInclusive 20 ; sh:message "수위는 1~20 m (표 6-1)" ] .

koai:WaterTempObsShape a sh:NodeShape ;
  sh:targetClass koai:WaterTempObservation ;
  sh:property [ sh:path qudt:unit ; sh:name "단위 ℃" ; sh:minCount 1 ; sh:maxCount 1 ; sh:hasValue unit:DEG_C ] ;
  sh:property [ sh:path sosa:hasSimpleResult ; sh:name "수온 0~50℃" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:float ; sh:minInclusive 0 ; sh:maxInclusive 50 ; sh:message "수온은 0~50℃ (표 6-1)" ] .
```

### B.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서B_TTAK.KO-10.1530_shapes.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:fbe9d8d2ff09a78baaf163c9f7b58bf89c4b36fddb38cba6e18b0ed3eeb2af5b` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 C QUDT/UCUM 단위 정의

**(본 부속서는 표준 내용의 일부임)**

### C.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ③ 데이터 모델의 증빙이다.

### C.2 설계

4.5의 단위 결합을 기계가독 형식으로 둔 것이다. 각 단위를 `qudt:unit`(QUDT 단위 IRI, 규범)과 `qudt:ucumCode`(UCUM 코드, 비-RDF 소비자용)로 함께 기술하며, UCUM 코드는 QUDT 공식 어휘의 값을 그대로 옮겼다. 원 표준이 단위를 복수 허용하는 요소는 허용 단위를 모두 등재하고, (단위, 범위) 짝의 검증은 SHACL 형상이 `sh:or`로 수행한다.

### C.3 수록본 (병행형 · 정본)

파일 `부속서/부속서C_TTAK.KO-10.1530_units.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1530 부속서 C — QUDT/UCUM 단위 정의  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# 단위 매핑 부속서 — TTAK.KO-10.1530 (유수식 스마트 수산양식 시스템의 센서 데이터 구조)
# 프로파일 ② 자기기술형 레코드 · AI-Ready 구성요소: 데이터 모델(L2) / 시맨틱(L1)
#
# [해결하는 문제]
#   원 표준의 ValueUnit은 표시용 코드로만 정의되어 기계가 해석할 수 없다.
#   (분석카드 A축 '단위 표기 모호성': 코드 0x0B 'm/L'은 본문 표 6-1 단위 목록에 없는 미사용 단위)
#   측정값 7.2가 pH인지 용존산소(mg/L)인지 기계가 판단할 근거가 없다.
#
# [해결 방식 — 두 경로를 함께 둔다]
#   1) RDF/그래프 경로 : qudt:unit 으로 QUDT 단위 IRI를 가리킨다 (규범).
#   2) 비-RDF 경로     : qudt:ucumCode 로 UCUM 코드 문자열을 싣는다.
#      @context를 해석하지 않는 소비자(센서 게이트웨이·기존 계측 시스템)에게
#      'unit:MilliGM-PER-L'은 뜻을 알 수 없는 문자열이지만 'mg.L-1'은 그 자체로 국제 표준 코드다.
#      또한 UCUM은 문법이므로 코드를 파싱하면 차원 계산·단위 변환이 바로 된다(IRI는 조회해야 안다).
#      QUDT가 qudt:ucumCode 로 두 표기의 공식 다리를 제공한다.
#
# [출처] 아래 ucumCode 값은 QUDT 공식 vocab(http://qudt.org/vocab/unit/<local>)의
#        qudt:ucumCode 를 그대로 옮긴 것이다(2026-07 확인). 임의로 만든 값이 없다.
#        UCUM은 지수 표기를 쓰므로 'mg/L'이 아니라 "mg.L-1" 이다 — 표 6-1의 표시 문자열과 다르다.
#
# [미해결 — 원 표준의 후속 조치 필요]
#   ① 탁도(NTU)는 UCUM에 정의가 없어 QUDT IRI(unit:NTU)만 둔다. UCUM 코드 없음이 정상이다.
#   ③ 표 6-1은 센서에 따라 단위를 복수로 허용하고(용존CO2 mg/L·ppm·%, 용존산소 mg/L·%,
#      염도 g/kg·ppt·ppm, 탁도 NTU·mg/L) 허용 범위가 단위마다 다르다. 이 부속서는 그 단위를
#      모두 등재하며, (단위, 범위) 짝의 검증은 부속서 B가 sh:or 로 수행한다.
#   ② ValueUnit 코드값(0x__)과 아래 단위의 대응표는 원 표준의 표 7-2를 재발행해야 확정된다.
#      현행 표 7-2는 0x0B 'm/L' 오류를 포함하므로 이 부속서에서는 코드번호를 확정하지 않고,
#      표 6-1이 명시한 센서별 측정 단위를 기준으로 대상 단위만 규정한다.

@prefix koai: <https://std.tta.or.kr/ns/koai#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix unit: <http://qudt.org/vocab/unit/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dcterms: <http://purl.org/dc/terms/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dcterms:license <https://creativecommons.org/licenses/by/4.0/> .

koai:ValueUnitScheme a skos:ConceptScheme ;
  skos:prefLabel "TTAK.KO-10.1530 센서 측정 단위"@ko ;
  rdfs:comment "표 6-1 센서별 측정 단위를 QUDT 단위 IRI 및 UCUM 코드에 결합한 목록."@ko .

# 수소이온농도 — pH (무차원)
koai:unit-pH a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "pH"@ko ; rdfs:comment "표 6-1 표기: pH · 측정범위 0~14"@ko ;
  qudt:unit unit:PH ; qudt:ucumCode "[pH]"^^qudt:UCUMcs .

# 수온 — 섭씨온도
koai:unit-degC a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "℃"@ko ; rdfs:comment "표 6-1 표기: ℃ · 수온 측정범위 0~50"@ko ;
  qudt:unit unit:DEG_C ; qudt:ucumCode "Cel"^^qudt:UCUMcs .

# 유량 — 분당 리터
koai:unit-LPerMin a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "L/min"@ko ; rdfs:comment "표 6-1 표기: L/min · 유량 측정범위 2~3600"@ko ;
  qudt:unit unit:L-PER-MIN ; qudt:ucumCode "L.min-1"^^qudt:UCUMcs .

# 용존CO2 · 용존산소 — 리터당 밀리그램
koai:unit-mgPerL a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "mg/L"@ko ;
  rdfs:comment "표 6-1 표기: mg/L · 용존CO2 0~20, 용존산소 0~50"@ko ;
  qudt:unit unit:MilliGM-PER-L ; qudt:ucumCode "mg.L-1"^^qudt:UCUMcs .

# 염도 — 킬로그램당 그램
koai:unit-gPerKg a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "g/kg"@ko ; rdfs:comment "표 6-1 표기: g/kg · 염도 측정범위 5~60"@ko ;
  qudt:unit unit:GM-PER-KiloGM ; qudt:ucumCode "g.kg-1"^^qudt:UCUMcs .

# 산화환원전위(ORP) — 밀리볼트
koai:unit-mV a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "mV"@ko ; rdfs:comment "표 6-1 표기: mV · ORP 측정범위 -1000~1400"@ko ;
  qudt:unit unit:MilliV ; qudt:ucumCode "mV"^^qudt:UCUMcs .

# 전도도 — 센티미터당 마이크로지멘스
koai:unit-uSPerCm a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "μS/cm"@ko ; rdfs:comment "표 6-1 표기: μS/cm · 전도도 측정범위 0~200"@ko ;
  qudt:unit unit:MicroS-PER-CentiM ; qudt:ucumCode "uS.cm-1"^^qudt:UCUMcs .

# 탁도 — NTU (UCUM 미정의)
koai:unit-NTU a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "NTU"@ko ;
  rdfs:comment "표 6-1 표기: NTU · 탁도 측정범위 0~4000. UCUM에 정의가 없어 QUDT IRI만 사용한다. 표 6-1은 같은 탁도에 mg/L(0~4500)도 허용하므로 부속서 B는 두 단위를 모두 통과시킨다."@ko ;
  qudt:unit unit:NTU .

# 용존CO2 · 염도 — 백만분율 (표 6-1이 mg/L과 함께 허용)
koai:unit-ppm a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "ppm"@ko ;
  rdfs:comment "표 6-1 표기: ppm · 용존CO2 0~20, 염도 0~50000"@ko ;
  qudt:unit unit:PPM ; qudt:ucumCode "[ppm]"^^qudt:UCUMcs .

# 용존CO2 · 용존산소 — 백분율(포화도) (표 6-1이 mg/L과 함께 허용)
koai:unit-percent a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "%"@ko ;
  rdfs:comment "표 6-1 표기: % · 용존CO2 0~200, 용존산소 0~200"@ko ;
  qudt:unit unit:PERCENT ; qudt:ucumCode "%"^^qudt:UCUMcs .

# 염도 — 천분율 (표 6-1이 g/kg과 함께 허용)
koai:unit-ppt a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "ppt"@ko ;
  rdfs:comment "표 6-1 표기: ppt · 염도 측정범위 0~50"@ko ;
  qudt:unit unit:PPTH ; qudt:ucumCode "[ppth]"^^qudt:UCUMcs .

# 수위 — 미터
koai:unit-m a skos:Concept ; skos:inScheme koai:ValueUnitScheme ;
  skos:prefLabel "m"@ko ; rdfs:comment "표 6-1 표기: m · 수위 측정범위 1~20"@ko ;
  qudt:unit unit:M ; qudt:ucumCode "m"^^qudt:UCUMcs .
```

### C.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서C_TTAK.KO-10.1530_units.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:ed36d20b693392e40e751779ace0c3d1f41f44e9e5aa62c515ead3414b7dae22` |
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
| 엔티티 (prov:Entity) | 데이터셋·파일 등 산출물 | ex:obs-20240131-1320, ex:tank-01 |
| 활동 (prov:Activity) | 데이터 생성·처리 활동 | pH 센서 주기 센싱 |
| 주체 (prov:Agent) | 생성자·발행처·지원기관 | ex:ph-sensor-01, OO계측(주) |
| 계보 관계 | 위 세 축을 잇는 관계 | 생성(wasGeneratedBy) · 귀속(wasAttributedTo) · 연관(wasAssociatedWith) · 사용(used) |

### D.3 수록본 (병행형 · 정본)

파일 `부속서/부속서D_TTAK.KO-10.1530_prov.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1530 부속서 D — PROV-O 출처 그래프  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# PROV-O 계보 예시 — TTAK.KO-10.1530 (센서 관측 출처, 출처/계보 L2 신설)
# 현재 출처/계보 0(미충족). 관측값이 어느 센서에서·언제 생성됐는지, 센서 제조·설치 이력을 PROV-O로 신설.
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix koai: <https://std.tta.or.kr/ns/koai#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/aqua/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

ex:obs-20240131-1320 a prov:Entity, sosa:Observation ;
  sosa:observedProperty ex:ph ;
  sosa:hasSimpleResult "7.8"^^xsd:float ;
  sosa:resultTime "2024-01-31T13:20:00"^^xsd:dateTime ;
  prov:wasGeneratedBy ex:sensing-activity ;
  prov:wasAttributedTo ex:ph-sensor-01 .

ex:sensing-activity a prov:Activity ;
  dct:description "pH 센서 주기 센싱" ;
  prov:startedAtTime "2024-01-31T13:20:00"^^xsd:dateTime ;
  prov:used ex:ph-sensor-01 ;
  prov:wasAssociatedWith ex:ph-sensor-01 .

ex:ph-sensor-01 a prov:Agent, sosa:Sensor ;
  dct:identifier "DEV-PH-01" ;
  koai:manufacturer "OO계측" ;
  dct:created "2024-01-01T00:00:00"^^xsd:dateTime ;    # InstallTime → 설치 이력
  prov:wasAttributedTo ex:manufacturer .

ex:manufacturer a prov:Agent, prov:Organization ;
  foaf:name "OO계측(주)" .

ex:tank-01 a prov:Entity, koai:WaterTank ;
  dct:identifier "TANK-01" .
ex:ph-sensor-01 prov:atLocation ex:tank-01 .
```

### D.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서D_TTAK.KO-10.1530_prov.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:d817108776a960b7316a0a402418998a647c82da677b54b643d614930b0ea812` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부록 (자유 작성) 참조구현 안내

이 표준은 참조구현을 공개하지 아니한다. 향후 공개하는 경우 이 부록에 위치·언어·라이선스를 적고, 참조구현은 표준의 일부가 아니며 협회는 그 내용에 대하여 보증하지 아니한다는 문구를 함께 둔다(운영요령 제19조의3제8항).

## 부록 (자유 작성) 원 표준 대비 교정 사항

원 표준의 현행 진단에서 확인된 정합성 결함(6건 — 데이터 타입 오기 2건(xs:short 비트폭·xs:float 정밀도), 단위 어휘 미결합, 코드 유효값 오류, 절 번호·요소명 불일치 등 6건)을 이 개정에서 본문·부속서로 교정했다. 교정 결과는 자가점검표 2부에 적었다.
