-- 코드를 작성해주세요
-- 아이템의 희귀도가 'RARE'인 아이템
-- 다음 업그레이드 아이템

SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO as I join ITEM_TREE as T on I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IN (SELECT I.ITEM_ID
                           FROM ITEM_INFO as I join ITEM_TREE as T 
                           on I.ITEM_ID = T.ITEM_ID 
                          WHERE I.RARITY = "RARE")
ORDER BY I.ITEM_ID DESC;