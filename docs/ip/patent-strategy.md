---
orphan: true
---

> Draft operational policy; not legal advice; not a contract.
> Subject to qualified legal review before any binding use.
> Korea first-to-file rule applies; consult a Korean patent
> attorney before any further public disclosure of candidate
> inventions.

# Patent strategy

Korea uses the first-to-file rule. Public disclosure before filing
narrows what can later be claimed. The strategy below is a
classification procedure for candidate inventions, not a list of
specific inventions. Specific inventions are *not* described in
detail in this public file; doing so would itself be public
disclosure.

## Classification before any further public disclosure

Each candidate invention is sorted into exactly one of these
categories before further publication, talks, posts, or external
demos:

| Category | Treatment |
| --- | --- |
| **Already publicly disclosed** | Record the disclosure, date and scope; seek jurisdiction-specific review of any remaining options. Publication does not itself dedicate copyright or other rights to the public domain. |
| **Not public yet** | The invention has not been published. A decision is required before any public release. |
| **Patent candidate** | A decision has been made to seek patent protection. Filing must precede any further public disclosure. |
| **Trade secret candidate** | The invention is best protected by keeping it confidential, not by patent. See [trade secret policy](trade-secret-policy.md). |
| **Defensive publication candidate** | Consider an authorized, dated technical disclosure after review. Do not promise that publication prevents all third-party filings or claims. |

## Procedure before disclosure

1. Identify the smallest novel claim. Distinguish from prior art the
   project is already aware of.
2. Classify into one of the categories above. If the classification
   is unclear, default to **not public yet** and seek legal advice.
3. If the classification is **patent candidate**, obtain qualified review
   of the filing and disclosure sequence before releasing details. Do not
   infer priority or patentability from this planning document.
4. If the classification is **trade secret candidate**, treat the
   material under the [trade secret policy](trade-secret-policy.md);
   it does not enter the open repositories.
5. If the classification is **defensive publication**, publish in a
   way that establishes timestamp and authorship (a public, dated
   write-up under the project's name).

## Categories of candidates (no specific naming)

The following categories of work in PCCX may contain candidate
inventions. **No specific inventions are listed by name in this
public file**; that listing lives in confidential project records
and goes through legal review before any further movement.

- Quantization and arithmetic-pipeline behaviour at the boundary
  between activations and weights.
- Memory-bound Transformer scheduling structures specific to the
  KV-cache traffic profile.
- Custom ISA encodings and decode strategies tuned for the
  decoupled-dataflow microarchitecture.
- Compiler / runtime techniques that map model graphs onto the
  IP-core's instruction stream.
- Verification harness techniques that produce reproducible
  evidence packs from a single trace.

Listing categories is not equivalent to listing inventions. Anyone
seeking to identify specific inventions must go through the
project's confidential disclosure procedure, not this page.

## Status

No patents have been filed by the project as of this page. No
specific patent candidates are publicly named. The procedure above
is the operational rule that runs before any further talk, paper,
demo, or release.
