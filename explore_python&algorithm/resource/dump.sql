BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text,regdate text);
INSERT INTO "users" VALUES(1,'Hong','hongreat95@gmail.com','010-0000-0000','winter.com','2021-12-18 23:4934');
INSERT INTO "users" VALUES(2,'winter','winter@naver.com','010-1111-1111','winter.com','2021-12-18 23:4934');
INSERT INTO "users" VALUES(3,'karina','karina@gmail.com','010-3333-3333','karina.com','2021-12-18 23:4934');
INSERT INTO "users" VALUES(4,'nayeon','nayeon@gmail.com','010-4444-4444','nayeon.com','2021-12-18 23:4934');
INSERT INTO "users" VALUES(5,'sana','sana@gmail.com','010-5555-5555','sana.com','2021-12-18 23:4934');
COMMIT;
