# Data Formats Documentation

This document describes the structure and schema for each data file used by the CareerAI project. These formats are required for reliable parsing, validation, and agent operation (e.g., LlamaIndex).

---

## 1. `experience.md`

- **Type:** Markdown
- **Purpose:** Contains professional experience entries in Markdown format.
- **Format:**
  - Each job/role is a section with a heading (##), followed by details and bullet points.
  - Recommended fields: Title, Company, Dates, Location, Bullet points for achievements/responsibilities.
- **Example:**

  ```markdown
  ## Software Engineer, Acme Corp

  **Dates:** Jan 2021 – Present  
  **Location:** Remote

  - Developed scalable backend services using Python and FastAPI.
  ```

---

## 2. `education.json`

- **Type:** JSON (list of objects)
- **Purpose:** Stores education history.
- **Schema:**
  - `institution` (str, required): Name of the institution
  - `degree` (str, required): Degree obtained
  - `field_of_study` (str, required): Major/field
  - `start_year` (int, required): Start year
  - `end_year` (int, required): End year
  - `location` (str, required): Location
- **Example:**
  ```json
  [
    {
      "institution": "State University",
      "degree": "B.Sc. Computer Science",
      "field_of_study": "Computer Science",
      "start_year": 2015,
      "end_year": 2019,
      "location": "Springfield, IL"
    }
  ]
  ```

---

## 3. `skills.json`

- **Type:** JSON (list of objects)
- **Purpose:** Lists user skills and optional proficiency.
- **Schema:**
  - `name` (str, required): Skill name
  - `proficiency` (str, optional): Proficiency level (e.g., Beginner, Intermediate, Advanced, Expert)
- **Example:**
  ```json
  [
    { "name": "Python", "proficiency": "Expert" },
    { "name": "Project Management" }
  ]
  ```

---

## 4. `user_data.json`

- **Type:** JSON (object)
- **Purpose:** Stores user profile information.
- **Schema:**
  - `name` (str, required): Full name
  - `email` (str, required): Email address
  - `location` (str, required): Location
  - `summary` (str, required): Brief professional summary
- **Example:**
  ```json
  {
    "name": "Jane Doe",
    "email": "jane.doe@email.com",
    "location": "Remote",
    "summary": "Experienced software engineer..."
  }
  ```

---

## 5. `summary.md`

- **Type:** Markdown
- **Purpose:** Contains a brief professional summary in Markdown format.
- **Format:**
  - One or more paragraphs summarizing the user's professional background.
- **Example:**

  ```markdown
  # Professional Summary

  Experienced software engineer with 5+ years in backend development...
  ```

---

# Why Documentation is Required

- Ensures the LlamaIndex agent and all function tools can reliably parse and validate data.
- Prevents errors due to unexpected or malformed data.
- Serves as a contract for UI/backend integration and future contributors.
- Enables schema validation and automated tooling.
