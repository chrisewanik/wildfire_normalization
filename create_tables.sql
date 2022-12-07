-- Drop any tables that already exist
drop table if exists final_project.ignitions CASCADE;


-- Create Data Table

create table final_project.ignitions (
	FIRE_ID serial, 
	SRC_AGENCY text, 
	FIRENAME text,
	LATITUDE varchar(50),
	LONGITUDE VARCHAR(50),
	YEAR NUMERIC,
	MONTH NUMERIC,
	DAY NUMERIC,
	REP_DATE date,
	ATTK_DATE date,
	OUT_DATE date,
	DECADE text,
	SIZE_HA NUMERIC,
	CAUSE text,
	PROTZONE text,
	FIRE_TYPE text,
	MORE_INFO text,
	CFS_REF_ID text,
	CFS_NOTE1 text,
	CFS_NOTE2 text,
	ACQ_DATE date,
	SRC_AGY2 text,
	ECOZONE NUMERIC,
	ECOZ_REF text,
	ECOZ_NAME text,
	ECOZ_NOM text,
	geometry geometry
	
);


select * FROM final_project.ignitions;