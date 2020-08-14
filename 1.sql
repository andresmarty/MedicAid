CREATE TABLE obra_social
(
 id    bigint NOT NULL PRIMARY KEY,
 nombre text NOT NULL UNIQUE
);


CREATE TABLE paciente
(
 id               bigint NOT NULL PRIMARY KEY,
 cuil             text NOT NULL,
 nombre           text NOT NULL,
 apellido           text NOT NULL,
 dni              text NULL,
 fecha_nacimiento timestamp NULL,
 obra_social_id   bigint REFERENCES obra_social ( id )
);

CREATE TABLE importe
(
 id             bigint NOT NULL PRIMARY KEY,
 honorarios     decimal NULL,
 fijo           decimal NULL,
 obra_social_id bigint NOT NULL REFERENCES obra_social ( id ),
 fecha_inicio   timestamp NOT NULL,
 fecha_fin      timestamp NULL,
 tipo           text NOT NULL,
 estado         text NOT NULL
);

CREATE TABLE practica
(
 id             bigint NOT NULL PRIMARY KEY,
 fecha          timestamp NULL,
 tipo           text NOT NULL,
 estado         text NOT NULL,
 importe_id     bigint NOT NULL REFERENCES importe ( id ),
 obra_social_id bigint NOT NULL REFERENCES obra_social ( id )
);

CREATE TABLE parto
(
 id                 bigint NOT NULL PRIMARY KEY,
 estado             text NOT NULL,
 fecha_de_parto         timestamp NULL,
 paciente_id        bigint NOT NULL REFERENCES Paciente ( id ),
 fecha_menstruacion timestamp NOT NULL,
 practica_id        bigint NOT NULL ( practica_id ) REFERENCES practica ( id )
);










