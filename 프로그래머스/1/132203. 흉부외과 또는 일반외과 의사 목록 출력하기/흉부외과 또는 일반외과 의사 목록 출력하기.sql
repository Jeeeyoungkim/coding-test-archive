-- 코드를 입력하세요

-- 진료과가 CS거나 GS
-- 고용일자 내림차순, 이름은 오름차순

SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") as HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' or MCDP_CD = 'GS'
ORDER BY HIRE_YMD desc, DR_NAME