-- 코드를 입력하세요
-- 총주문량 > 3000
-- 주성분이 과일
-- 총주문량 내림차순

SELECT F.FLAVOR
FROM FIRST_HALF AS F JOIN ICECREAM_INFO AS I ON F.FLAVOR = I.FLAVOR
WHERE TOTAL_ORDER > 3000 and I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC