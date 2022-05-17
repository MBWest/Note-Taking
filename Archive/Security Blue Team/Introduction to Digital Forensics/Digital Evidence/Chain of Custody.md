# Chain of Custody

**Chain of Custody is the**
> Logical sequence of gathering evidence, whether it be physical or electronic in legal cases

**If this process is not followed properly, the evidence collected may be rendered inadmissible in court, so legal prosecution can\'t take place.**

- It is important to have a record of who collected a piece of evidence, and who has been responsible for it since it was collected.

- If an Analyst is conducting a forensic investigation on a hard-drive image, they should NOT be working on the original copy of the evidence. The original disk image should be hashed (the mathematical calculation which results in a unique text string specific to that exact file) and then a full bit copy should be taken, ensuring that absolutely everything is included in the copied image. This new file should then be hashed, and if it is an exact copy, the file hashes will be the same. The Analyst should then work on the copy, so the original evidence is not modified, making it inadmissible in court.

- When copying evidence to a forensic disk (a high capacity hard-drive used only for forensic investigations or incident response), the storage media should be completely sanitised, to ensure that there is no data already on it, as this could contaminate the evidence.