---

## Get issues associated with a single PR. (V0)
### input:
- PR Number
- loginOrg
- repo

### output:
Return:
- A list of issues as described below
- Or and empty list if there was an error or if there were no issues associated with the PR

**The list of** issue objects as defined in the graphql schema
- For **each Issue**
   - Required:
     - URL as unique id
     - title
     - labels as a comma separated list of strings enclosed in quotes
     - state

### Error handling. What returns in the list of issues?
- If the PR is not found, return an empty list.
- If the PR is found, but there are no issues associated with it, return an empty list.
- If there is any type of exception found,  return an empty list.
- Exceptions include:
  - malformed graphql
  - network errors



---

## Get issues associated with a single PR. (V1)
## 

### input:
- PR Number
- loginOrg
- repo

### output:
Return a Tuple of:
- The return code which will indicate success or have an error code
- The list of issues
- The error message or the word "Success"


**The list of** issue objects as defined in the graphql schema
- For **each Issue**
   - Required:
     - URL as unique id
     - title
     - labels as a comma separated list of strings enclosed in quotes
     - state
     - **list of** project objects as defined in the graphql schema
     - For **each project**
       - Required
         - project URL as unique id
         - values of of all fields defined within that project
           - The intent of this is to make sure things like the OG Queue will be returned. See: [Decision table for comparing contents of Backlog and Sprint](https://docs.google.com/spreadsheets/d/1nOwITq9rITgg2T-RCvKB8YqtN1kSENekY0DNcIB7rF8/edit?usp=sharing)

### Error handling. What returns in the list of issues?
- If the PR is not found, return an empty list.
- If the PR is found, but there are no issues associated with it, return an empty list.
- If there is any type of exception found,  return an empty list.
- Exceptions include:
  - malformed graphql
  - network errors


## Get issue by URL
input: 
- URL to an item of type Issue

output: 
- An issue object as defined in the graphql schema
- For each Issue
   - Required: 
     - URL as unique id
     - title
     - labels
     - state
     - list of project objects as defined in the graphql schema
     - For each project
       - Required
         - project URL as unique id
         - values of all fields defined within that project
           - The intent of this is to make sure things like the OG Queue will be returned. See: [Decision table for comparing contents of Backlog and Sprint](https://docs.google.com/spreadsheets/d/1nOwITq9rITgg2T-RCvKB8YqtN1kSENekY0DNcIB7rF8/edit?usp=sharing)
           
               

