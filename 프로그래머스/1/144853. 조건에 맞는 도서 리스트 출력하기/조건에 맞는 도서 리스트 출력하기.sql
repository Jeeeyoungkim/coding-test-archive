-- 코드를 입력하세요
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE from BOOK where CATEGORY = "인문" and DATE_FORMAT(PUBLISHED_DATE, '%Y') = "2021" order by BOOK_ID desc