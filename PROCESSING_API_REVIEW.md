# Processing API Documentation Review

## Summary of Confusing Elements Fixed

As a developer trying to use the Mapflow API, the following issues in `source/api/processing_api.rst` would have caused confusion:

### 🔴 Critical Issues Fixed

1. **Empty "Get user status" section** (Line ~18)
   - **Problem**: Section header with empty table - no endpoint, no example
   - **Fixed**: Added proper endpoint `GET /rest/user/status` with description
   - **Impact**: Developers couldn't discover available models/workflow definitions

2. **Broken "processings/stats" request** (Lines ~180-200)
   - **Problem**: JSON request truncated mid-object (`"page": 1,` then abruptly ends)
   - **Fixed**: Completed the JSON with proper fields and moved to separate section
   - **Impact**: Copy-paste would fail; unclear what fields are required

3. **Nested table chaos** (Lines ~180-400)
   - **Problem**: `POST /processings/v2` endpoint embedded *inside* the stats table, then cost/v2 embedded inside "Rename project"
   - **Fixed**: Properly separated all sections with correct heading levels
   - **Impact**: Impossible to tell where one endpoint ends and another begins

4. **Missing closing braces** (Line ~458)
   - **Problem**: "Rename project" JSON example missing `}`
   - **Fixed**: Added closing brace
   - **Impact**: Invalid JSON examples

5. **"▶️ Run the processing" section confusion** (Lines ~1145-1170)
   - **Problem**: Heading says "Run processing" but shows `GET /processings` (list endpoint), then text says "Runs an imagery analysis"
   - **Fixed**: Renamed to "Create and run processing (v1)" with proper `POST` endpoint
   - **Impact**: Mixed GET (read) with POST (create) semantics - very confusing!

### 🟡 Moderate Issues Fixed

6. **Duplicate v1 endpoints**
   - **Problem**: v1 list/get endpoints appeared early in file (lines 30-180) AND again under "Processing API v1" (lines 1000+)
   - **Fixed**: Kept early ones as-is (legacy position), clarified v1 section focuses on create/run
   - **Impact**: Developers unsure which section is canonical

7. **Malformed "Processing status" table** (Lines ~1510-1550)
   - **Problem**: 
     - `AWAITING` has no description
     - Random list-table inserted mid-table
     - `CANCELLED` duplicated with different wording
   - **Fixed**: Merged into single clean table, removed duplicate
   - **Impact**: Unclear what each status means

8. **"Customize processing" incomplete example** (Line ~1180)
   - **Problem**: Shows only `blocks` field, omitting required fields like `projectId`, `wdName`, `geometry`
   - **Fixed**: Added note "Partial request body example (include this inside the create request above)"
   - **Impact**: Developers might try to POST just `{"blocks": [...]}` which would fail

9. **v1/v2 mixing** throughout
   - **Problem**: v1 and v2 endpoints interleaved without clear separation
   - **Fixed**: Added clear "Processing API v2" and "Processing API v1" sections
   - **Impact**: Developers unsure which params structure to use

### 🟢 Minor Issues Fixed

10. **Typos**
    - "desctiptions" → "descriptions"
    - "URl" → "URL"

11. **Upload images reference** (Line ~980)
    - **Problem**: References `:ref:\`Create processing\`` which doesn't exist as a named anchor
    - **Fixed**: Provided explicit v1/v2 param paths instead
    - **Impact**: Broken internal link

12. **Inconsistent heading levels**
    - **Problem**: v2 subsections used `^^^^^^` (h2) instead of `"""""` (h3)
    - **Fixed**: Aligned all v2 GET endpoints as h3 under v2 h2
    - **Impact**: TOC/navigation broken

---

## Key Improvements for Developers

### ✅ Clear workflow now visible:

**v2 (recommended):**
1. GET `/rest/user/status` → discover models
2. POST `/rest/projects` → create project
3. POST `/rest/processings/v2` → create & run processing with `sourceParams`/`inferenceParams`
4. GET `/rest/processings/{id}/v2` → check status
5. GET `/rest/processings/{id}/result` → download results

**v1 (legacy):**
- Same flow but uses flat `params` map instead of nested objects

### ✅ All JSON examples now valid and complete
- No truncated objects
- All required fields present or clearly marked optional
- Proper closing braces

### ✅ Sections properly separated
- No tables nested inside other tables
- Clear h2/h3 hierarchy
- v1 and v2 clearly distinguished

---

## Remaining Considerations

1. **Should v1 be marked deprecated?** Currently v1 and v2 co-exist without clear recommendation
2. **Cost endpoint appears in both v1 and v2** - are both needed?
3. **"Customize processing" section** is under v1 but applies to both - might need its own section
4. **Reference tables at end** assume readers know the difference between v1 flat params and v2 nested params

---

## Build Status

✅ Sphinx build succeeded with no errors or warnings after changes.
