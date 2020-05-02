CREATE TABLE user
(
  username VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  user_ID VARCHAR(50) NOT NULL,
  user_cards VARCHAR(50) NOT NULL,
  type VARCHAR(50) NOT NULL,
  PRIMARY KEY (user_ID)
);

CREATE TABLE collections
(
  cardName VARCHAR(50) NOT NULL,
  size VARCHAR(50) NOT NULL,
  collection_ID VARCHAR(50) NOT NULL,
  user_ID VARCHAR(50) NOT NULL,
  PRIMARY KEY (collection_ID),
  FOREIGN KEY (user_ID) REFERENCES user(user_ID)
);

CREATE TABLE sales
(
  cardName VARCHAR(50) NOT NULL,
  outletName VARCHAR(50) NOT NULL,
  outlet_ID VARCHAR(50) NOT NULL,
  sellerName VARCHAR(50) NOT NULL,
  seller_id VARCHAR(50) NOT NULL,
  buyer_id VARCHAR(50) NOT NULL,
  user_ID VARCHAR(50) NOT NULL,
  PRIMARY KEY (outlet_ID),
  FOREIGN KEY (user_ID) REFERENCES user(user_ID)
);

CREATE TABLE user_cards
(
  game VARCHAR(50) NOT NULL,
  card_id VARCHAR(50) NOT NULL,
  collection_ID VARCHAR(50) NOT NULL,
  outlet_ID VARCHAR(50) NOT NULL,
  PRIMARY KEY (card_id),
  FOREIGN KEY (collection_ID) REFERENCES collections(collection_ID),
  FOREIGN KEY (outlet_ID) REFERENCES sales(outlet_ID)
);

CREATE TABLE Cards
(
  cardName VARCHAR(50) NOT NULL,
  cardPrice VARCHAR(50) NOT NULL,
  price VARCHAR(50) NOT NULL,
  card_id VARCHAR(50) NOT NULL,
  FOREIGN KEY (card_id) REFERENCES user_cards(card_id)
);

