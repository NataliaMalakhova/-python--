--
-- PostgreSQL database dump
--

-- Dumped from database version 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.20 (Ubuntu 12.20-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: characters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.characters (
    id integer NOT NULL,
    birth_year character varying,
    eye_color character varying,
    films text,
    gender character varying,
    hair_color character varying,
    height character varying,
    homeworld character varying,
    mass character varying,
    name character varying,
    skin_color character varying,
    species text,
    starships text,
    vehicles text
);


ALTER TABLE public.characters OWNER TO postgres;

--
-- Name: characters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.characters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.characters_id_seq OWNER TO postgres;

--
-- Name: characters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.characters_id_seq OWNED BY public.characters.id;


--
-- Name: characters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters ALTER COLUMN id SET DEFAULT nextval('public.characters_id_seq'::regclass);


--
-- Data for Name: characters; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.characters (id, birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles) FROM stdin;
1	19BBY	blue	1, 2, 3, 6	male	blond	172	https://swapi.dev/api/planets/1/	77	Luke Skywalker	fair		12, 22	14, 30
3	33BBY	red	1, 2, 3, 4, 5, 6	n/a	n/a	96	https://swapi.dev/api/planets/8/	32	R2-D2	white, blue	2		
6	52BBY	blue	1, 5, 6	male	brown, grey	178	https://swapi.dev/api/planets/1/	120	Owen Lars	light			
9	24BBY	brown	1	male	black	183	https://swapi.dev/api/planets/1/	84	Biggs Darklighter	light		12	
2	112BBY	yellow	1, 2, 3, 4, 5, 6	n/a	n/a	167	https://swapi.dev/api/planets/1/	75	C-3PO	gold	2		
4	41.9BBY	yellow	1, 2, 3, 6	male	none	202	https://swapi.dev/api/planets/1/	136	Darth Vader	white		13	
7	47BBY	blue	1, 5, 6	female	brown	165	https://swapi.dev/api/planets/1/	75	Beru Whitesun lars	light			
5	19BBY	brown	1, 2, 3, 6	female	brown	150	https://swapi.dev/api/planets/2/	49	Leia Organa	light			30
8	unknown	red	1	n/a	n/a	97	https://swapi.dev/api/planets/1/	32	R5-D4	white, red	2		
12	64BBY	blue	1, 6	male	auburn, grey	180	https://swapi.dev/api/planets/21/	unknown	Wilhuff Tarkin	fair			
10	57BBY	blue-gray	1, 2, 3, 4, 5, 6	male	auburn, white	182	https://swapi.dev/api/planets/20/	77	Obi-Wan Kenobi	fair		48, 59, 64, 65, 74	38
11	41.9BBY	blue	4, 5, 6	male	blond	188	https://swapi.dev/api/planets/1/	84	Anakin Skywalker	fair		39, 59, 65	44, 46
13	200BBY	blue	1, 2, 3, 6	male	brown	228	https://swapi.dev/api/planets/14/	112	Chewbacca	unknown	3	10, 22	19
14	29BBY	brown	1, 2, 3	male	brown	180	https://swapi.dev/api/planets/22/	80	Han Solo	fair		10, 22	
15	44BBY	black	1	male	n/a	173	https://swapi.dev/api/planets/23/	74	Greedo	green	4		
19	unknown	blue	1	male	brown	180	https://swapi.dev/api/planets/26/	110	Jek Tono Porkins	fair		12	
18	21BBY	hazel	1, 2, 3	male	brown	170	https://swapi.dev/api/planets/22/	77	Wedge Antilles	fair		12	14
16	600BBY	orange	1, 3, 4	hermaphrodite	n/a	175	https://swapi.dev/api/planets/24/	1,358	Jabba Desilijic Tiure	green-tan, brown	5		
22	31.5BBY	brown	2, 3, 5	male	black	183	https://swapi.dev/api/planets/10/	78.2	Boba Fett	fair		21	
21	82BBY	yellow	2, 3, 4, 5, 6	male	grey	170	https://swapi.dev/api/planets/8/	75	Palpatine	pale			
24	53BBY	red	2	male	none	190	https://swapi.dev/api/planets/29/	113	Bossk	green	7		
27	41BBY	orange	3	male	none	180	https://swapi.dev/api/planets/31/	83	Ackbar	brown mottle	8		
26	37BBY	blue	2	male	none	175	https://swapi.dev/api/planets/6/	79	Lobot	light			
25	31BBY	brown	2, 3	male	black	177	https://swapi.dev/api/planets/30/	79	Lando Calrissian	dark		10	
20	896BBY	brown	2, 3, 4, 5, 6	male	white	66	https://swapi.dev/api/planets/28/	17	Yoda	green	6		
23	15BBY	red	2	none	none	200	https://swapi.dev/api/planets/28/	140	IG-88	metal	2		
30	8BBY	brown	3	male	brown	88	https://swapi.dev/api/planets/7/	20	Wicket Systri Warrick	brown	9		
29	unknown	brown	3	male	brown	unknown	https://swapi.dev/api/planets/28/	unknown	Arvel Crynyd	fair		28	
28	48BBY	blue	3	female	auburn	150	https://swapi.dev/api/planets/32/	unknown	Mon Mothma	fair			
31	unknown	black	3	male	none	160	https://swapi.dev/api/planets/33/	68	Nien Nunb	grey	10	10	
34	91BBY	blue	4	male	blond	170	https://swapi.dev/api/planets/9/	unknown	Finis Valorum	fair			
32	92BBY	blue	4	male	brown	193	https://swapi.dev/api/planets/28/	89	Qui-Gon Jinn	fair			38
33	unknown	red	4, 5, 6	male	none	191	https://swapi.dev/api/planets/18/	90	Nute Gunray	mottled green	11		
36	52BBY	orange	4, 5	male	none	196	https://swapi.dev/api/planets/8/	66	Jar Jar Binks	orange	12		
37	unknown	orange	4	male	none	224	https://swapi.dev/api/planets/8/	82	Roos Tarpals	grey	12		
35	46BBY	brown	4, 5, 6	female	brown	185	https://swapi.dev/api/planets/8/	45	Padmé Amidala	light		39, 49, 64	
38	unknown	orange	4	male	none	206	https://swapi.dev/api/planets/8/	unknown	Rugor Nass	green	12		
40	unknown	yellow	4, 5	male	black	137	https://swapi.dev/api/planets/34/	unknown	Watto	blue, grey	13		
39	unknown	blue	4	male	brown	183	https://swapi.dev/api/planets/8/	unknown	Ric Olié	fair		40	
42	62BBY	brown	4	male	black	183	https://swapi.dev/api/planets/8/	unknown	Quarsh Panaka	dark			
43	72BBY	brown	4, 5	female	black	163	https://swapi.dev/api/planets/1/	unknown	Shmi Skywalker	fair			
41	unknown	orange	4	male	none	112	https://swapi.dev/api/planets/35/	40	Sebulba	grey, red	14		
45	unknown	pink	3	male	none	180	https://swapi.dev/api/planets/37/	unknown	Bib Fortuna	pale	15		
44	54BBY	yellow	4	male	none	175	https://swapi.dev/api/planets/36/	80	Darth Maul	red	22	41	42
50	unknown	orange	4	male	none	163	https://swapi.dev/api/planets/41/	65	Ben Quadinaros	grey, green, yellow	19		
46	48BBY	hazel	4, 5, 6	female	none	178	https://swapi.dev/api/planets/37/	55	Ayla Secura	blue	15		
49	unknown	black	4	male	none	122	https://swapi.dev/api/planets/40/	unknown	Gasgano	white, blue	18		
47	unknown	unknown	4	male	none	79	https://swapi.dev/api/planets/38/	15	Ratts Tyerel	grey, blue	16		
51	72BBY	brown	4, 5, 6	male	none	188	https://swapi.dev/api/planets/42/	84	Mace Windu	dark			
52	92BBY	yellow	4, 5, 6	male	white	198	https://swapi.dev/api/planets/43/	82	Ki-Adi-Mundi	pale	20		
48	unknown	yellow	4	male	none	94	https://swapi.dev/api/planets/39/	45	Dud Bolt	blue, grey	17		
54	unknown	brown	4, 6	male	black	171	https://swapi.dev/api/planets/45/	unknown	Eeth Koth	brown	22		
53	unknown	black	4, 5, 6	male	none	196	https://swapi.dev/api/planets/44/	87	Kit Fisto	green	21		
55	unknown	blue	4, 6	female	none	184	https://swapi.dev/api/planets/9/	50	Adi Gallia	dark	23		
57	unknown	yellow	4	male	none	264	https://swapi.dev/api/planets/48/	unknown	Yarael Poof	white	25		
59	unknown	blue	4, 5	male	none	196	https://swapi.dev/api/planets/50/	unknown	Mas Amedda	blue	27		
62	82BBY	blue	5	male	brown	183	https://swapi.dev/api/planets/1/	unknown	Cliegg Lars	fair			
61	unknown	brown	5	female	brown	157	https://swapi.dev/api/planets/8/	unknown	Cordé	light			
58	22BBY	black	4, 5, 6	male	none	188	https://swapi.dev/api/planets/49/	80	Plo Koon	orange	26	48	
56	unknown	orange	4, 6	male	none	188	https://swapi.dev/api/planets/47/	unknown	Saesee Tiin	pale	24		
64	58BBY	blue	5, 6	female	black	170	https://swapi.dev/api/planets/51/	56.2	Luminara Unduli	yellow	29		
63	unknown	yellow	5, 6	male	none	183	https://swapi.dev/api/planets/11/	80	Poggle the Lesser	green	28		
60	unknown	brown	5	male	black	185	https://swapi.dev/api/planets/8/	85	Gregar Typho	dark		39	
65	40BBY	blue	5	female	black	166	https://swapi.dev/api/planets/51/	50	Barriss Offee	yellow	29		
66	unknown	brown	5	female	brown	165	https://swapi.dev/api/planets/8/	unknown	Dormé	light	1		
68	67BBY	brown	5, 6	male	black	191	https://swapi.dev/api/planets/2/	unknown	Bail Prestor Organa	tan	1		
69	66BBY	brown	5	male	black	183	https://swapi.dev/api/planets/53/	79	Jango Fett	tan			
78	unknown	black	5, 6	female	none	178	https://swapi.dev/api/planets/58/	57	Shaak Ti	red, blue, white	35		
67	102BBY	brown	5, 6	male	white	193	https://swapi.dev/api/planets/52/	80	Dooku	fair	1		55
75	unknown	red, blue	5, 6	female	none	96	https://swapi.dev/api/planets/28/	unknown	R4-P17	silver, red			
77	unknown	gold	5	male	none	191	https://swapi.dev/api/planets/57/	unknown	San Hill	grey	34		
79	unknown	green, yellow	6	male	none	216	https://swapi.dev/api/planets/59/	159	Grievous	brown, white	36	74	60
81	unknown	brown	1, 6	male	brown	188	https://swapi.dev/api/planets/2/	79	Raymus Antilles	light			
72	unknown	black	5	male	none	229	https://swapi.dev/api/planets/10/	88	Lama Su	grey	32		
70	unknown	yellow	5	female	blonde	168	https://swapi.dev/api/planets/54/	55	Zam Wesell	fair, green, yellow	30		45
73	unknown	black	5	female	none	213	https://swapi.dev/api/planets/10/	unknown	Taun We	grey	32		
71	unknown	yellow	5	male	none	198	https://swapi.dev/api/planets/55/	102	Dexter Jettster	brown	31		
74	unknown	blue	5	female	white	167	https://swapi.dev/api/planets/9/	unknown	Jocasta Nu	fair	1		
76	unknown	unknown	5	male	none	193	https://swapi.dev/api/planets/56/	48	Wat Tambor	green, grey	33		
80	unknown	blue	6	male	brown	234	https://swapi.dev/api/planets/14/	136	Tarfful	brown	3		
82	unknown	white	5, 6	female	none	178	https://swapi.dev/api/planets/60/	48	Sly Moore	pale			
\.


--
-- Name: characters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.characters_id_seq', 1, false);


--
-- Name: characters characters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.characters
    ADD CONSTRAINT characters_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

