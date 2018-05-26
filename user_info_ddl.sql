CREATE TABLE user_info (
  `username` varchar(255) NOT NULL,
  `user_info` varchar(2500) NOT NULL,
  PRIMARY KEY (`username`)
)

INSERT INTO user_info(username, user_info) VALUES ('jinhai', 'A good cat.');
INSERT INTO user_info(username, user_info) VALUES ('dest', 'A bad drgn.');
INSERT INTO user_info(username, user_info) VALUES ('catbot', 'BEST CAT.');
INSERT INTO user_info(username, user_info) VALUES ('h', 'h');

