-- Programmers 04/30 2022
-- 우유와 요거트가 담긴 장바구니

SELECT DISTINCT A.CART_ID
FROM (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Yogurt') A
INNER JOIN (SELECT CART_ID FROM CART_PRODUCTS WHERE NAME = 'Milk') B
ON A.CART_ID = B.CART_ID