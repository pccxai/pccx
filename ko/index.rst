========================================
PCCX 문서
========================================

PCCX (Parallel Compute Core eXecutor)는 Altifigence가 시작하고 운영하는
오픈소스 반도체 프로젝트입니다. 공개 RTL·검증 환경·기술 문서를 함께
발전시킵니다. SystemVerilog 개발자는 :doc:`docs/quickstart`\ 에서 시작하세요.

프로젝트
--------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-ecosystem-grid

   .. grid-item-card:: :octicon:`cpu;1.2em;sd-mr-1` v002 RTL
      :link: https://github.com/pccxai/pccx-v002
      :link-type: url

      재사용 가능한 RTL, 테스트벤치, Sail ISA 모델. 작은 검증 기여의 출발점입니다.

   .. grid-item-card:: :octicon:`cpu;1.2em;sd-mr-1` KV260 통합
      :link: https://github.com/pccxai/pccx-FPGA-NPU-LLM-kv260
      :link-type: url

      고정된 코어를 사용하는 보드 통합과 런타임. 실제 보드 결과는 별도로 검증합니다.

   .. grid-item-card:: :octicon:`book;1.2em;sd-mr-1` 문서 소스
      :link: https://github.com/pccxai/pccx
      :link-type: url

      이 사이트의 영어·한국어 문서와 기여 안내입니다.

   .. grid-item-card:: :octicon:`beaker;1.2em;sd-mr-1` 실험 단계의 v003
      :link: https://github.com/pccxai/pccx-v003
      :link-type: url

      v003 RTL과 검증 작업. 소스 공개가 하드웨어 검증 완료를 뜻하지 않습니다.

참여와 검증
------------

.. grid:: 1 1 2 2
   :gutter: 3 4 4 4
   :class-container: pccx-toolchain-grid

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` 기여 시작
      :link: docs/onboarding/getting-started
      :link-type: doc

      지금 가능한 로컬 점검과 시뮬레이션의 남은 의존성을 확인하세요.

   .. grid-item-card:: :octicon:`project-roadmap;1.2em;sd-mr-1` 공개 참여 로드맵
      :link: docs/roadmap
      :link-type: doc

      기존 작업 정리 → 독립적인 RTL 테스트 → 작은 검증 이슈 → 외부 PR.

   .. grid-item-card:: :octicon:`verified;1.2em;sd-mr-1` 검증과 증거
      :link: docs/Evidence/index
      :link-type: doc

      시뮬레이션·합성·실제 보드 실행의 근거를 구분합니다.

   .. grid-item-card:: :octicon:`terminal;1.2em;sd-mr-1` Digital Design Studio
      :link: https://docs.altifigence.com/ide/
      :link-type: url

      선택적으로 참고할 Altifigence 도구 문서. PCCX 참여에 특정 IDE를 요구하지 않습니다.

.. note::

   pccx-lab, SystemVerilog IDE, PCCX Launcher는 폐지되었습니다.
   폐지 도구의 남은 의존성 제거는 :doc:`docs/roadmap`\ 에서 추적합니다.

.. toctree::
   :maxdepth: 2
   :caption: 소개

   docs/index
   docs/quickstart
   docs/onboarding/getting-started
   docs/Evidence/index
   docs/roadmap

.. toctree::
   :maxdepth: 1
   :caption: v002 아키텍처

   docs/v002/index

.. toctree::
   :maxdepth: 1
   :caption: 타겟 하드웨어

   docs/Devices/index

.. toctree::
   :maxdepth: 1
   :caption: 아카이브

   docs/archive/index

.. toctree::
   :maxdepth: 1
   :caption: 외부 링크

   Digital Design Studio <https://docs.altifigence.com/ide/>
   Altifigence.com <https://altifigence.com/>
   PCCX Transparency <https://pccx.ai/ko-kr/legal/transparency/>
