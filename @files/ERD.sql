CREATE TABLE `user`(
	id int(11) auto_increment primary key,
	username varchar(50),
	password varchar(32),
	status enum('0','1'),
	created_at timestamp DEFAULT CURRENT_TIMESTAMP,
	updated_at datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
INSERT INTO user (name, username, password, status) VALUES ('admin', md5('admin'), '1');
