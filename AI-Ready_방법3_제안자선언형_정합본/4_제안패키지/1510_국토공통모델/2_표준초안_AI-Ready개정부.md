# TTAK.KO-10.1510 AI-Ready 개정 표준초안(개정부) — 디지털 국토정보 플랫폼의 데이터 연계를 위한 공통 데이터 모델
정보통신단체표준(국문표준) · TTAK.KO-10.1510 · 제정 2024.12.06 · AI-Ready 개정 제안 · 소관 PG409 (공간정보) · 에디터 건국대학교 산학협력단

> 이 초안은 **AI-Ready 개정부 중심**으로 작성되었다. 원 표준의 도메인 본문(적용범위·용어·요소 상세)은 원 표준을 계승·참조하고, AI-Ready 개정으로 새로 추가·강화되는 부분 — 인용 표준 보강(2절), 요소 정의표의 전역 어휘 식별자(4절), 기계가독 부속서(5절·부속서), 참조구현 안내(부록) — 을 실제로 채웠다. 절 번호와 양식은 「정보통신단체표준 작성지침(TTAR-09.0040)」과 그 AI-Ready 개정안(6.5.3·6.5.7·6.6·6.7)을 따른다.

> **작성 주체.** 요소 정의표의 전역 어휘 식별자(IRI) 매핑과 모든 부속서는 **에디터**가 제안 단계의 「기계가독 산출물 선언서」(별지 제11-1호서식)에 따라 작성했다(운영요령 제19조의3제1항, 작성지침 6.5.7). 별도의 공동 에디터(어휘 전문가)를 두지 아니한다. 선언과의 일치는 상정 시 자가점검표(별지 제21-1호서식) 3부에서 확인한다.

## 서문

이 표준은 「디지털 국토정보 플랫폼의 데이터 연계를 위한 공통 데이터 모델」의 개정판이다. 원 표준(제정 2024.12.06)의 적용범위와 데이터 구조를 계승하되, 데이터를 사람과 기계가 함께 읽을 수 있도록 각 데이터 요소의 의미를 전역 어휘 식별자(IRI)에 매핑하고, 그 매핑을 JSON-LD @context로 배포하며, 값 제약·출처·품질·이용조건을 기계가독 부속서로 제공한다. 이로써 이 표준을 따르는 데이터는 별도 해석 없이 상호운용·검증·재이용이 가능해진다.

**AI-Ready 목표 수준** — 기술 대상 프로파일 ② 자기기술형 레코드 (공간 객체 레코드) · 필수 시맨틱 · 신태틱 · 데이터 모델 · 권장 + 출처 (= L2). (근거: 첨부 「기계가독 산출물 선언서」 및 「AI-Ready 자가점검표」)

## 1. 적용범위

이 표준은 「디지털 국토정보 플랫폼의 데이터 연계를 위한 공통 데이터 모델」이 규정하는 데이터의 요소·구조·값 형식을 계승하며(원 표준 1절 참조), 그 데이터 요소를 전역 어휘에 매핑하여 기계가독 형식으로 배포하기 위한 요소 정의·인용 표준·부속서 구성을 규정한다. 원 표준의 도메인 규정은 변경 없이 유지되고, 이 개정은 그 위에 기계가독 계층을 더한다.

## 2. 인용 표준

다음 표준·어휘는 이 표준의 적용에 필수적이며, 본문에서 인용되는 범위에서 이 표준의 일부를 구성한다. 선언서 2에서 선언한 외부 어휘를 **모두** 등재한다(작성지침 6.5.3 · 운영요령 제19조제1항제9호). 종전에 참고 문헌에 두었던 어휘도 요소 의미가 규범적으로 의존하므로 인용 표준으로 올린다.

| 인용 표준 · 어휘 | 발행 주체 | 이 표준에서의 용도(접두어) | 사용 방식 |
|---|---|---|---|
| JSON-LD 1.1 | W3C | 요소↔IRI 매핑의 규범 직렬화(부속서 A) | 직렬화 규격 |
| GeoSPARQL 1.1 | OGC | geo: 기하·WKT 리터럴 | IRI로 가리킴 |
| Simple Features Access (SFA) | OGC | sf: 기하 유형(점·선·면) | IRI로 가리킴 |
| Semantic Sensor Network (SOSA/SSN) | W3C | sosa: 관측 결과·시각 | IRI로 가리킴 |
| DCMI Metadata Terms | DCMI | dct: 식별자·생성일·갱신일·출처 | IRI로 가리킴 |
| SKOS Simple Knowledge Organization System | W3C | skos: 건물 용도·등급 분류 | IRI로 가리킴 |
| PROV-O: The PROV Ontology | W3C | prov: 데이터 생성 내력(권장) | IRI로 가리킴 |
| Shapes Constraint Language (SHACL) | W3C | sh: 값 검증 언어 — 부속서 B | IRI로 가리킴 |
| FOAF Vocabulary | FOAF Project | foaf: 부속서 C에서 사용 | IRI로 가리킴 |
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

이 절이 AI-Ready 개정의 핵심이며, 모든 기계가독 부속서가 파생되는 원천이다. 원 표준이 정의한 데이터 요소 29개 전체를 작성지침 6.5.7의 요소 정의표로 규정한다(이 표준 필수 M 10개 · 권장 R 5개). 컬럼이 14개로 많으므로 <표 6-5>의 허용에 따라 표를 둘로 나누었다 — <표 4-1>은 값의 형식(요소 이름·표시명·데이터 유형·값 영역·다중성·필수 여부·단위), <표 4-2>는 어휘 바인딩(요소 이름·출처·버전·전역 어휘 식별자·비고)이다.

> **개정부 초안의 범위.** 14개 컬럼 가운데 **정의·기본값·예시**는 원 표준의 요소 상세를 그대로 계승하므로 이 개정부 초안에서는 생략하고, 통합본 작성 시 <표 6-5>에 따라 모두 채운다. 다중성·필수 여부는 소속 객체 기준이다(예: 파라미터 이름은 "파라미터가 있으면 반드시"). '권장'은 원 표준의 R(권장)을 뜻하며 작성지침의 필수 여부 구분(필수·선택·조건부)에서는 선택에 해당하므로 비고에 적었다.

### 4.1 객체(클래스)

요소가 소속되는 객체다. 객체는 값을 갖지 않으므로 다중성·필수 여부는 해당 없음이다.

| 객체 이름 | 표시명 | 출처 | 전역 어휘 식별자(IRI) |
|---|---|---|---|
| `Building` | 건물 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/dln#Building`) |
| `BuildingRoom` | 건물 실 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/dln#BuildingRoom`) |
| `BuildingInstallation` | 건물 설비 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/dln#BuildingInstallation`) |
| `CityFurniture` | 도시 시설물 | 이 표준 | 자체 정의 (`https://std.tta.or.kr/ns/dln#CityFurniture`) |

### 4.2 요소 — 값의 형식 <표 4-1>

| 요소 이름 | 표시명 | 데이터 유형 | 값 영역 | 다중성 | 필수 여부 | 단위 |
|---|---|---|---|---|---|---|
| `cityObjectMemberId` | 객체 식별자 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `gisBuildingId` | GIS 건물 ID | 문자열 | 건축물생성년도 4 + 위치정보(x,y) 16 + 층별정보(지상_지하) 5 + 호별정보 3 · 길이 28자리 | 0..1 | 선택 | 해당 없음 |
| `ufid` | 국토관리번호(UFID) | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `jusoBuildingId` | 주소기반 건물 ID | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `dtmName` | 수치지형도명 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `dtmCode` | 레이어 코드 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `geometryType` | 기하 유형 | 코드 | 점 · 선 · 면 | 1 | 필수 | 해당 없음 |
| `mapScale` | 축척 | 문자열 | 제한 없음 | 0..1 | 선택 | 비율 |
| `creationDate` | 생성일 | 날짜 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `updateDate` | 갱신일 | 날짜 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `geometry` | 기하 | 식별자(IRI) | 제한 없음 | 1 | 필수 | 해당 없음 |
| `asWKT` | 기하값(WKT) | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `storeysAboveGround` | 지상 층수 | 정수 | 0 이상 | 1 | 필수 | 해당 없음 |
| `storeysBelowGround` | 지하 층수 | 정수 | 0 이상 | 1 | 필수 | 해당 없음 |
| `xCoordinate` | X 좌표 | 문자열 | GRS80(EPSG:5186) · ^[0-9]+\.[0-9]{6,10}$ (원 표준 6.1.12) · 길이 소수점 6~10자리 | 1 | 필수 | m |
| `yCoordinate` | Y 좌표 | 문자열 | GRS80(EPSG:5186) · ^[0-9]+\.[0-9]{6,10}$ (원 표준 6.1.13) · 길이 소수점 6~10자리 | 1 | 필수 | m |
| `zCoordinate` | Z 좌표 | 문자열 | GRS80(EPSG:5186) · ^[0-9]+\.[0-9]{6,10}$ (원 표준 6.1.14) · 길이 소수점 6~10자리 | 0..1 | 선택 | m |
| `storeyName` | 층명 | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `BuildingClass` | 건물 등급 | 코드 | 코드 목록(부속서 B sh:in) | 0..1 | 선택 | 해당 없음 |
| `BuildingUsage` | 건물 용도 | 코드 | 코드 목록(부속서 B sh:in) | 0..1 | 선택 | 해당 없음 |
| `opendataId` | 공공데이터 ID | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `surfaceId` | 표면 ID | 문자열 | 제한 없음 | 1 | 필수 | 해당 없음 |
| `visValue` | 가시화 값 | 문자열 | 제한 없음 | 0..1 | 선택 | 해당 없음 |
| `observation` | 관측값 | 문자열 | 제한 없음 | 0..n | 선택 | 해당 없음 |
| `observedAt` | 관측 시각 | 날짜시간 | 제한 없음 | 0..1 | 선택 | 해당 없음 |

### 4.3 요소 — 어휘 바인딩 <표 4-2>

전역 어휘 식별자(IRI) 컬럼은 에디터가 선언서 2의 어휘 범위 안에서 작성했다. 자체 정의 요소는 '자체 정의'로 적고 비고에 이 표준의 네임스페이스 IRI를 밝힌다. 직렬화 키(@context의 키)는 요소 이름과 같다.

| 요소 이름 | 출처 | 버전 | 전역 어휘 식별자(IRI) | 비고 |
|---|---|---|---|---|
| `cityObjectMemberId` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/identifier` | 해당 없음 |
| `gisBuildingId` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#gisBuildingId` |
| `ufid` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#ufid` |
| `jusoBuildingId` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#jusoBuildingId` |
| `dtmName` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/source` | 해당 없음 |
| `dtmCode` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#layerCode` |
| `geometryType` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#geometryType` |
| `mapScale` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#mapScale` |
| `creationDate` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/created` | 권장 |
| `updateDate` | DCMI Metadata Terms | 이번 AI-Ready 개정판 | `http://purl.org/dc/terms/modified` | 권장 |
| `geometry` | GeoSPARQL 1.1 | 이번 AI-Ready 개정판 | `http://www.opengis.net/ont/geosparql#hasGeometry` | 해당 없음 |
| `asWKT` | GeoSPARQL 1.1 | 이번 AI-Ready 개정판 | `http://www.opengis.net/ont/geosparql#asWKT` | 리터럴 유형 geo:wktLiteral |
| `storeysAboveGround` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#storeysAboveGround` |
| `storeysBelowGround` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#storeysBelowGround` |
| `xCoordinate` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#xCoordinate` |
| `yCoordinate` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#yCoordinate` |
| `zCoordinate` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#zCoordinate` |
| `storeyName` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#storeyName` |
| `BuildingClass` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#buildingClass` · 권장 |
| `BuildingUsage` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#buildingUsage` · 권장 |
| `opendataId` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#opendataId` |
| `surfaceId` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#surfaceId` |
| `visValue` | 이 표준 | 이번 AI-Ready 개정판 | 자체 정의 | 네임스페이스 `https://std.tta.or.kr/ns/dln#visValue` |
| `observation` | Semantic Sensor Network (SOSA/SSN) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/sosa/hasSimpleResult` | 해당 없음 |
| `observedAt` | Semantic Sensor Network (SOSA/SSN) | 이번 AI-Ready 개정판 | `http://www.w3.org/ns/sosa/resultTime` | 해당 없음 |

### 4.4 코드·열거값

코드(열거) 유형 요소의 허용값이다. 부속서의 SHACL 형상에서 `sh:in` 제약으로 검증한다.

| 요소 | 허용값 목록 |
|---|---|
| dln:geometryType(dln:geometryType) | 점 · 선 · 면 |

### 4.6 형상 전체에 걸리는 값 제약

요소 하나에 대응하지 않는 규칙(택일·범위 조합·특정 노드 대상)은 요소 정의표가 아니라 여기에 적고, SHACL 형상에서 `sh:or`·`sh:targetNode` 등으로 표현한다.

| 적용 대상 | 값 범위 · 유효 조건 |
|---|---|
| x좌표(GRS80) | x좌표는 소수점 6~10자리(EPSG:5186) |
| dln:Building | 기하 유형은 점·선·면 중 하나 |

## 5. 기계가독 산출물 및 부속서

이 표준을 따르는 데이터의 기계가독 표현은 다음 부속서로 제공한다(운영요령 제19조의3, 작성지침 6.6). 요소 정의표는 4절 본문이며 부속서가 아니다. 별표(★)는 이 표준의 기술 대상 프로파일에서 필수 산출물이다.

| 부속서 | 산출물 | 구성요소 | 형태 | 제공 파일 | 필수/권장 |
|---|---|---|---|---|---|
| 부속서 A | JSON-LD @context | ② 신태틱 | 병행형(작성지침 6.6 a) | `부속서/부속서A_TTAK.KO-10.1510_context.jsonld` | ★ 필수 |
| 부속서 B | SHACL 형상(값 제약 검증) | ③ 데이터 모델 | 병행형(작성지침 6.6 a) | `부속서/부속서B_TTAK.KO-10.1510_shapes.ttl` | ★ 필수 |
| 부속서 C | PROV-O 출처 그래프 | ④ 출처/계보 | 병행형(작성지침 6.6 a) | `부속서/부속서C_TTAK.KO-10.1510_prov.ttl` | 권장 |

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
| geo | `http://www.opengis.net/ont/geosparql#` |
| sf | `http://www.opengis.net/ont/sf#` |
| sosa | `http://www.w3.org/ns/sosa/` |
| dct | `http://purl.org/dc/terms/` |
| skos | `http://www.w3.org/2004/02/skos/core#` |
| prov | `http://www.w3.org/ns/prov#` |
| dln | `https://std.tta.or.kr/ns/dln#` |
| xsd | `http://www.w3.org/2001/XMLSchema#` |

### A.3 수록본 (병행형 · 정본)

파일 `부속서/부속서A_TTAK.KO-10.1510_context.jsonld`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
{
  "$comment": "TTAK.KO-10.1510 부속서 A — JSON-LD @context (본 부속서는 표준 내용의 일부임). 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/. 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다(운영요령 제19조의3제2항). 근거: 운영요령 제19조의3제7항, 작성지침 6.6.",
  "http://purl.org/dc/terms/license": { "@id": "https://creativecommons.org/licenses/by/4.0/" },
  "@context": {
    "@version": 1.1,
    "geo": "http://www.opengis.net/ont/geosparql#",
    "sf": "http://www.opengis.net/ont/sf#",
    "sosa": "http://www.w3.org/ns/sosa/",
    "dct": "http://purl.org/dc/terms/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "dln": "https://std.tta.or.kr/ns/dln#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "Building": "dln:Building",
    "BuildingRoom": "dln:BuildingRoom",
    "BuildingInstallation": "dln:BuildingInstallation",
    "CityFurniture": "dln:CityFurniture",

    "cityObjectMemberId": { "@id": "dct:identifier", "@type": "xsd:string" },
    "gisBuildingId": "dln:gisBuildingId",
    "ufid": "dln:ufid",
    "jusoBuildingId": "dln:jusoBuildingId",
    "dtmName": "dct:source",
    "dtmCode": "dln:layerCode",
    "geometryType": { "@id": "dln:geometryType", "@type": "@vocab" },
    "mapScale": "dln:mapScale",
    "creationDate": { "@id": "dct:created", "@type": "xsd:date" },
    "updateDate": { "@id": "dct:modified", "@type": "xsd:date" },

    "geometry": { "@id": "geo:hasGeometry", "@type": "@id" },
    "asWKT": { "@id": "geo:asWKT", "@type": "geo:wktLiteral" },
    "storeysAboveGround": { "@id": "dln:storeysAboveGround", "@type": "xsd:integer" },
    "storeysBelowGround": { "@id": "dln:storeysBelowGround", "@type": "xsd:integer" },
    "xCoordinate": "dln:xCoordinate",
    "yCoordinate": "dln:yCoordinate",
    "zCoordinate": "dln:zCoordinate",
    "storeyName": "dln:storeyName",

    "BuildingClass": { "@id": "dln:buildingClass", "@type": "@vocab" },
    "BuildingUsage": { "@id": "dln:buildingUsage", "@type": "@vocab" },

    "opendataId": "dln:opendataId",
    "surfaceId": "dln:surfaceId",
    "visValue": "dln:visValue",
    "observation": { "@id": "sosa:hasSimpleResult" },
    "observedAt": { "@id": "sosa:resultTime", "@type": "xsd:dateTime" }
  },
  "_meta": {
    "standard": "TTAK.KO-10.1510",
    "title": "디지털 국토정보 플랫폼의 데이터 연계를 위한 공통 데이터 모델",
    "profile": "② 자기기술형 레코드(공간객체)",
    "note": "OGC CityGML 3.0 프로파일. 좌표(GRS80/EPSG:5186)는 GeoSPARQL geo:asWKT로, 코드리스트(BuildingClass 등)는 SKOS로, Dynamizer 시계열 공공데이터는 SOSA Observation으로. dln 접두어는 본 표준 확장 네임스페이스."
  }
}
```

### A.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서A_TTAK.KO-10.1510_context.jsonld` |
| 형식 | JSON-LD |
| 무결성 확인 값 | `sha256:1398ea1629aa531d7883523dae80e20cb3da27ddfa26d4f59e95bbe3932c73c2` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 B SHACL 형상(값 제약 검증)

**(본 부속서는 표준 내용의 일부임)**

### B.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ③ 데이터 모델의 증빙이다.

### B.2 설계

4절 요소 정의표의 필수 여부·다중성·값 영역을 SHACL 형상으로 옮긴 것이다. 필수 여부와 다중성은 `sh:minCount`·`sh:maxCount`로, 값 범위는 `sh:minInclusive`·`sh:maxInclusive`로, 허용값(코드)은 `sh:in`으로, 길이·형식은 `sh:pattern`·`sh:minLength`·`sh:maxLength`로, 단위는 `sh:hasValue` 또는 `sh:in`으로 대응한다. 형상 전체에 걸리는 규칙(4.6)은 `sh:or`·`sh:closed`·`sh:targetNode`로 표현한다. 요소 정의표를 고치면 이 형상을 다시 생성한다.

### B.3 수록본 (병행형 · 정본)

파일 `부속서/부속서B_TTAK.KO-10.1510_shapes.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1510 부속서 B — SHACL 형상(값 제약 검증)  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# SHACL 검증 스키마 — TTAK.KO-10.1510
# 재생성: 요소 정의표(원천)의 M(필수)/R/O·카디널리티로 minCount/maxCount 구동.
# 값 제약(층수 하한·좌표 형식)은 원 표준 6.1.12~6.1.14 및 3D 건물 속성 정의에서 옮긴다.

@prefix brick: <https://brickschema.org/schema/Brick#> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dcam: <http://purl.org/dc/dcam/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcmitype: <http://purl.org/dc/dcmitype/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix dln: <https://std.tta.or.kr/ns/dln#> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix geo: <http://www.opengis.net/ont/geosparql#> .
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
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

dln:BuildingShape a sh:NodeShape ;
  sh:targetClass dln:Building ;
  sh:property [ sh:path dct:created ; sh:name "생성일자" ; sh:maxCount 1 ; sh:datatype xsd:date ] ;
  sh:property [ sh:path dct:identifier ; sh:name "cityObjectMemberId" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path dct:modified ; sh:name "갱신일자" ; sh:maxCount 1 ; sh:datatype xsd:date ] ;
  sh:property [ sh:path dln:gisBuildingId ; sh:name "GIS건물통합 PK" ; sh:maxCount 1 ] ;
  sh:property [ sh:path dln:storeysAboveGround ; sh:name "지상 층수" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:integer ; sh:minInclusive 0 ; sh:message "지상 층수는 0 이상" ] ;
  sh:property [ sh:path dln:storeysBelowGround ; sh:name "지하 층수" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:integer ; sh:minInclusive 0 ; sh:message "지하 층수는 0 이상" ] ;
  sh:property [ sh:path dln:ufid ; sh:name "연속수치지형도 PK" ; sh:minCount 1 ; sh:maxCount 1 ; sh:datatype xsd:string ] ;
  sh:property [ sh:path geo:hasGeometry ; sh:name "기하" ; sh:minCount 1 ; sh:maxCount 1 ; sh:nodeKind sh:IRI ] .

dln:GeometryTypeShape a sh:NodeShape ;
  sh:targetClass dln:Building ;
  sh:property [ sh:path dln:geometryType ; sh:minCount 1 ; sh:maxCount 1 ; sh:in ( "점" "선" "면" ) ; sh:message "기하 유형은 점·선·면 중 하나" ] .

dln:OpendataLinkShape a sh:NodeShape ;
  sh:targetClass dln:OpendataLink ;
  sh:property [ sh:path dln:opendataId ; sh:name "공공데이터 PK" ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path dln:storeyName ; sh:name "층 정보" ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path dln:surfaceId ; sh:name "Surface ID" ; sh:minCount 1 ; sh:maxCount 1 ] ;
  sh:property [ sh:path dln:xCoordinate ; sh:name "x좌표(GRS80)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:pattern "^[0-9]+\\.[0-9]{6,10}$" ; sh:message "x좌표는 소수점 6~10자리(EPSG:5186 · 원 표준 6.1.12)" ] ;
  sh:property [ sh:path dln:yCoordinate ; sh:name "y좌표(GRS80)" ; sh:minCount 1 ; sh:maxCount 1 ; sh:pattern "^[0-9]+\\.[0-9]{6,10}$" ; sh:message "y좌표는 소수점 6~10자리(EPSG:5186 · 원 표준 6.1.13)" ] ;
  sh:property [ sh:path dln:zCoordinate ; sh:name "z좌표(GRS80)" ; sh:maxCount 1 ; sh:pattern "^[0-9]+\\.[0-9]{6,10}$" ; sh:message "z좌표는 소수점 6~10자리(EPSG:5186 · 원 표준 6.1.14)" ] .
```

### B.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서B_TTAK.KO-10.1510_shapes.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:43a913e66ad980cea50305a5f31c94c3b789ca4e2a41d504508ed1e84888d03f` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부속서 C PROV-O 출처 그래프

**(본 부속서는 표준 내용의 일부임)**

### C.1 규범성

이 부속서가 수록하는 기계가독 산출물은 본 표준의 규범 내용이다. 이 산출물에 적합하지 아니한 데이터·구현은 본 표준에 적합하다고 할 수 없다. 이 산출물은 별표 10 구성요소 ④ 출처/계보의 증빙이다.

### C.2 설계

데이터가 누구에 의해 어떤 활동으로 생성·파생됐는지를 PROV-O의 세 축 — 엔티티(데이터·산출물)·활동(생성·처리)·주체(사람·기관) — 과 계보 관계로 형식화한다. 이 부속서는 그 설계를 따른 **예시 인스턴스**이며, 표의 예시 값(기관·데이터세트 이름)은 표준이 특정 대상을 규정하는 것이 아니다. 요소를 참조할 때는 <표 4-2>의 IRI를 쓴다.

| PROV-O 구조 | 이 표준에서의 대응 | 예시 (부속서 C) |
|---|---|---|
| 엔티티 (prov:Entity) | 데이터셋·파일 등 산출물 | ex:building-0001, GIS건물통합정보, 연속수치지형도(건물통합정보_마스터) |
| 활동 (prov:Activity) | 데이터 생성·처리 활동 | 2D↔3D 건물 데이터 연계(ufid·gisBuildingId 매칭) |
| 주체 (prov:Agent) | 생성자·발행처·지원기관 | 국토교통부, 국토지리정보원, 디지털 국토정보 기술개발 사업단 |
| 계보 관계 | 위 세 축을 잇는 관계 | 생성(wasGeneratedBy) · 귀속(wasAttributedTo) · 파생(wasDerivedFrom) · 연관(wasAssociatedWith) · 사용(used) |

### C.3 수록본 (병행형 · 정본)

파일 `부속서/부속서C_TTAK.KO-10.1510_prov.ttl`과 같은 내용이다. 수록본과 제공 파일이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).

```
# ============================================================================
# TTAK.KO-10.1510 부속서 C — PROV-O 출처 그래프  (본 부속서는 표준 내용의 일부임)
# 이용조건(라이선스): CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/
# 정본은 표준 부속서 수록본이며 이 파일은 기계 처리용 제공본이다. 둘이 다를 경우 수록본에 따른다(운영요령 제19조의3제2항).
# 이용조건 표시 근거: 운영요령 제19조의3제7항 · 작성지침 6.6
# ============================================================================
# PROV-O 계보 예시 — TTAK.KO-10.1510 (연계 지도 출처, 출처/계보 L2)
# 건물 객체가 어떤 정부 지도(GIS건물통합·연속수치지형도·주소정보기본도)로부터 연계·생성됐는지 PROV-O로 형식화.
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix dln:  <https://std.tta.or.kr/ns/dln#> .
@prefix dct:  <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix ex:   <https://example.org/dln/> .

# 이 파일(문서) 자체의 이용조건 — 기계가 읽을 수 있도록 트리플로도 둔다.
<> dct:license <https://creativecommons.org/licenses/by/4.0/> .

ex:building-0001 a prov:Entity, dln:Building ;
  dct:identifier "B-0001" ;
  dct:created "2024-06-28"^^xsd:date ;
  dct:modified "2024-12-06"^^xsd:date ;
  prov:wasGeneratedBy ex:linkage-activity ;
  prov:wasDerivedFrom ex:gis-building, ex:continuous-map ;
  prov:wasAttributedTo ex:project-team .

ex:linkage-activity a prov:Activity ;
  dct:description "2D↔3D 건물 데이터 연계(ufid·gisBuildingId 매칭)" ;
  prov:used ex:gis-building, ex:continuous-map ;
  prov:generated ex:building-0001 ;
  prov:wasAssociatedWith ex:project-team ;
  prov:endedAtTime "2024-12-06T00:00:00"^^xsd:dateTime .

ex:gis-building a prov:Entity ;
  dct:title "GIS건물통합정보" ;
  dct:publisher ex:molit ;
  dln:gisBuildingId "2008196092914556429100000000" .

ex:continuous-map a prov:Entity ;
  dct:title "연속수치지형도(건물통합정보_마스터)" ;
  dct:publisher ex:ngii ;
  dln:ufid "..." .

ex:molit a prov:Agent, prov:Organization ; foaf:name "국토교통부" .
ex:ngii a prov:Agent, prov:Organization ; foaf:name "국토지리정보원" .
ex:project-team a prov:Agent, prov:Organization ; foaf:name "디지털 국토정보 기술개발 사업단" .
```

### C.4 제공 파일

| 항목 | 기재 |
|---|---|
| 파일 | `부속서/부속서C_TTAK.KO-10.1510_prov.ttl` |
| 형식 | Turtle |
| 무결성 확인 값 | `sha256:2da5c23b51ab22e1e53c8aa3dc4030d00a7c9b4596cfc06ab44bdf38da9bf414` |
| 이용조건 | CC BY 4.0 — 파일 머리말에 표시 |
| 정본 | 이 부속서의 수록본 |

## 부록 (자유 작성) 참조구현 안내

이 표준은 참조구현을 공개하지 아니한다. 향후 공개하는 경우 이 부록에 위치·언어·라이선스를 적고, 참조구현은 표준의 일부가 아니며 협회는 그 내용에 대하여 보증하지 아니한다는 문구를 함께 둔다(운영요령 제19조의3제8항).

## 부록 (자유 작성) 원 표준 대비 교정 사항

원 표준의 현행 진단에서 확인된 정합성 결함(2건 — 인용표준 분류 오류 1건(GeoSPARQL을 참고문헌에 둠), 좌표계 EPSG 코드 표기 불일치 1건)을 이 개정에서 본문·부속서로 교정했다. 교정 결과는 자가점검표 2부에 적었다.
