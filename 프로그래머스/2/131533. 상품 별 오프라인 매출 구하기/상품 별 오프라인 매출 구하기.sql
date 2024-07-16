SELECT P.PRODUCT_CODE, SUM(SALES_AMOUNT) * P.PRICE AS SALES
FROM PRODUCT P
INNER JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC , PRODUCT_CODE;