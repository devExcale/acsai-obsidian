# Schema Anomalies

Take as example the following schema and instance.

`Curriculum (Matr, TC, SurN, Name, BirthD, City, Prov, C#, Tit, Doc, Date, Grade)`

| Matr | TC  | SurN    | Name  | BirthD | City  | Prov | C#  | Tit       | Doc   | Date | Grade |
| ---- | --- | ------- | ----- | ------ | ----- | ---- | --- | --------- | ----- | ---- | ----- |
| 01   | ... | Rossi   | Mario | ...    | Tolfa | Rome | 10  | Physics   | Goofy | ...  | ...   |
| 02   | ... | Bianchi | Paolo | ...    | Tolfa | Rome | 10  | Physics   | Goofy | ...  | ...   |
| 01   | ... | Rossi   | Mario | ...    | Tolfa | Rome | 20  | Chemistry | Pluto | ...  | ...   |

Multiple anomalies can be noted. In detail,
- **Redundancy:** student's biographical data is stored for each exam taken by the student; course data is stored for each exam taken for that course.
- **Update anomaly:** if the professor of a course changes, the information has to be modified for each exam of that course

%% TK continue - slides 06 (good schema) %%
