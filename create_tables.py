table_statements = [
"""CREATE TABLE IF NOT EXISTS chaashto (
	aashtocl TEXT (254),
	rvindicator TEXT (3) NOT NULL,
	chkey TEXT (30) NOT NULL,
	chaashtokey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chconsistence (
	rupresblkmst TEXT (254),
	rupresblkdry TEXT (254),
	rupresblkcem TEXT (254),
	rupresplate TEXT (254),
	mannerfailure TEXT (254),
	stickiness TEXT (254),
	plasticity TEXT (254),
	rvindicator TEXT (3) NOT NULL,
	chkey TEXT (30) NOT NULL,
	chconsistkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chdesgnsuffix (
	desgnsuffix TEXT (254),
	chkey TEXT (30) NOT NULL,
	chdesgnsfxkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chfrags (
	fragvol_l INT16,
	fragvol_r INT16,
	fragvol_h INT16,
	fragkind TEXT (254),
	fragsize_l INT16,
	fragsize_r INT16,
	fragsize_h INT16,
	fragshp TEXT (254),
	fraground TEXT (254),
	fraghard TEXT (254),
	chkey TEXT (30) NOT NULL,
	chfragskey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chorizon (
	hzname TEXT (12),
	desgndisc INT16,
	desgnmaster TEXT (254),
	desgnmasterprime TEXT (254),
	desgnvert INT16,
	hzdept_l INT16,
	hzdept_r INT16,
	hzdept_h INT16,
	hzdepb_l INT16,
	hzdepb_r INT16,
	hzdepb_h INT16,
	hzthk_l INT16,
	hzthk_r INT16,
	hzthk_h INT16,
	fraggt10_l INT16,
	fraggt10_r INT16,
	fraggt10_h INT16,
	frag3to10_l INT16,
	frag3to10_r INT16,
	frag3to10_h INT16,
	sieveno4_l FLOAT64,
	sieveno4_r FLOAT64,
	sieveno4_h FLOAT64,
	sieveno10_l FLOAT64,
	sieveno10_r FLOAT64,
	sieveno10_h FLOAT64,
	sieveno40_l FLOAT64,
	sieveno40_r FLOAT64,
	sieveno40_h FLOAT64,
	sieveno200_l FLOAT64,
	sieveno200_r FLOAT64,
	sieveno200_h FLOAT64,
	sandtotal_l FLOAT64,
	sandtotal_r FLOAT64,
	sandtotal_h FLOAT64,
	sandvc_l FLOAT64,
	sandvc_r FLOAT64,
	sandvc_h FLOAT64,
	sandco_l FLOAT64,
	sandco_r FLOAT64,
	sandco_h FLOAT64,
	sandmed_l FLOAT64,
	sandmed_r FLOAT64,
	sandmed_h FLOAT64,
	sandfine_l FLOAT64,
	sandfine_r FLOAT64,
	sandfine_h FLOAT64,
	sandvf_l FLOAT64,
	sandvf_r FLOAT64,
	sandvf_h FLOAT64,
	silttotal_l FLOAT64,
	silttotal_r FLOAT64,
	silttotal_h FLOAT64,
	siltco_l FLOAT64,
	siltco_r FLOAT64,
	siltco_h FLOAT64,
	siltfine_l FLOAT64,
	siltfine_r FLOAT64,
	siltfine_h FLOAT64,
	claytotal_l FLOAT64,
	claytotal_r FLOAT64,
	claytotal_h FLOAT64,
	claysizedcarb_l FLOAT64,
	claysizedcarb_r FLOAT64,
	claysizedcarb_h FLOAT64,
	om_l FLOAT64,
	om_r FLOAT64,
	om_h FLOAT64,
	dbtenthbar_l FLOAT64,
	dbtenthbar_r FLOAT64,
	dbtenthbar_h FLOAT64,
	dbthirdbar_l FLOAT64,
	dbthirdbar_r FLOAT64,
	dbthirdbar_h FLOAT64,
	dbfifteenbar_l FLOAT64,
	dbfifteenbar_r FLOAT64,
	dbfifteenbar_h FLOAT64,
	dbovendry_l FLOAT64,
	dbovendry_r FLOAT64,
	dbovendry_h FLOAT64,
	partdensity FLOAT64,
	ksat_l FLOAT64,
	ksat_r FLOAT64,
	ksat_h FLOAT64,
	awc_l FLOAT64,
	awc_r FLOAT64,
	awc_h FLOAT64,
	wtenthbar_l FLOAT64,
	wtenthbar_r FLOAT64,
	wtenthbar_h FLOAT64,
	wthirdbar_l FLOAT64,
	wthirdbar_r FLOAT64,
	wthirdbar_h FLOAT64,
	wfifteenbar_l FLOAT64,
	wfifteenbar_r FLOAT64,
	wfifteenbar_h FLOAT64,
	wsatiated_l INT16,
	wsatiated_r INT16,
	wsatiated_h INT16,
	lep_l FLOAT64,
	lep_r FLOAT64,
	lep_h FLOAT64,
	ll_l FLOAT64,
	ll_r FLOAT64,
	ll_h FLOAT64,
	pi_l FLOAT64,
	pi_r FLOAT64,
	pi_h FLOAT64,
	aashind_l INT16,
	aashind_r INT16,
	aashind_h INT16,
	kwfact TEXT (254),
	kffact TEXT (254),
	caco3_l INT16,
	caco3_r INT16,
	caco3_h INT16,
	gypsum_l INT16,
	gypsum_r INT16,
	gypsum_h INT16,
	sar_l FLOAT64,
	sar_r FLOAT64,
	sar_h FLOAT64,
	ec_l FLOAT64,
	ec_r FLOAT64,
	ec_h FLOAT64,
	cec7_l FLOAT64,
	cec7_r FLOAT64,
	cec7_h FLOAT64,
	ecec_l FLOAT64,
	ecec_r FLOAT64,
	ecec_h FLOAT64,
	sumbases_l FLOAT64,
	sumbases_r FLOAT64,
	sumbases_h FLOAT64,
	ph1to1h2o_l FLOAT64,
	ph1to1h2o_r FLOAT64,
	ph1to1h2o_h FLOAT64,
	ph01mcacl2_l FLOAT64,
	ph01mcacl2_r FLOAT64,
	ph01mcacl2_h FLOAT64,
	freeiron_l FLOAT64,
	freeiron_r FLOAT64,
	freeiron_h FLOAT64,
	feoxalate_l FLOAT64,
	feoxalate_r FLOAT64,
	feoxalate_h FLOAT64,
	extracid_l FLOAT64,
	extracid_r FLOAT64,
	extracid_h FLOAT64,
	extral_l FLOAT64,
	extral_r FLOAT64,
	extral_h FLOAT64,
	aloxalate_l FLOAT64,
	aloxalate_r FLOAT64,
	aloxalate_h FLOAT64,
	pbray1_l FLOAT64,
	pbray1_r FLOAT64,
	pbray1_h FLOAT64,
	poxalate_l FLOAT64,
	poxalate_r FLOAT64,
	poxalate_h FLOAT64,
	ph2osoluble_l FLOAT64,
	ph2osoluble_r FLOAT64,
	ph2osoluble_h FLOAT64,
	ptotal_l FLOAT64,
	ptotal_r FLOAT64,
	ptotal_h FLOAT64,
	excavdifcl TEXT (254),
	excavdifms TEXT (254),
	cokey TEXT (30) NOT NULL,
	chkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS chpores (
	poreqty_l FLOAT64,
	poreqty_r FLOAT64,
	poreqty_h FLOAT64,
	poresize TEXT (254),
	porecont TEXT (254),
	poreshp TEXT (254),
	rvindicator TEXT (3) NOT NULL,
	chkey TEXT (30) NOT NULL,
	chporeskey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chstruct (
	structgrade TEXT (254),
	structsize TEXT (254),
	structtype TEXT (254),
	structid INT16,
	structpartsto INT16,
	chstructgrpkey TEXT (30) NOT NULL,
	chstructkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chstructgrpkey) REFERENCES chstructgrp(chstructgrpkey));""",

"""CREATE TABLE IF NOT EXISTS chstructgrp (
	structgrpname TEXT (254),
	rvindicator TEXT (3) NOT NULL,
	chkey TEXT (30) NOT NULL,
	chstructgrpkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chtext (
	recdate REALDATE,
	chorizontextkind TEXT (254),
	textcat TEXT (20),
	textsubcat TEXT (20),
	text TEXT,
	chkey TEXT (30) NOT NULL,
	chtextkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chtexture (
	texcl TEXT (254),
	lieutex TEXT (254),
	chtgkey TEXT (30) NOT NULL,
	chtkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chtgkey) REFERENCES chtexturegrp(chtgkey));""",

"""CREATE TABLE IF NOT EXISTS chtexturegrp (
	texture TEXT (30),
	stratextsflag TEXT (3) NOT NULL,
	rvindicator TEXT (3) NOT NULL,
	texdesc TEXT,
	chkey TEXT (30) NOT NULL,
	chtgkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS chtexturemod (
	texmod TEXT (254),
	chtkey TEXT (30) NOT NULL,
	chtexmodkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chtkey) REFERENCES chtexture(chtkey));""",

"""CREATE TABLE IF NOT EXISTS chunified (
	unifiedcl TEXT (254),
	rvindicator TEXT (3) NOT NULL,
	chkey TEXT (30) NOT NULL,
	chunifiedkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(chkey) REFERENCES chorizon(chkey));""",

"""CREATE TABLE IF NOT EXISTS cocanopycover (
	plantcov INT16,
	plantsym TEXT (8) NOT NULL,
	plantsciname TEXT (127),
	plantcomname TEXT (60),
	cokey TEXT (30) NOT NULL,
	cocanopycovkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cocropyld (
	cropname TEXT (254),
	yldunits TEXT (254),
	nonirryield_l FLOAT64,
	nonirryield_r FLOAT64,
	nonirryield_h FLOAT64,
	irryield_l FLOAT64,
	irryield_r FLOAT64,
	irryield_h FLOAT64,
	cropprodindex INT16,
	vasoiprdgrp TEXT (254),
	cokey TEXT (30) NOT NULL,
	cocropyldkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS codiagfeatures (
	featkind TEXT (254),
	featdept_l INT16,
	featdept_r INT16,
	featdept_h INT16,
	featdepb_l INT16,
	featdepb_r INT16,
	featdepb_h INT16,
	featthick_l INT16,
	featthick_r INT16,
	featthick_h INT16,
	cokey TEXT (30) NOT NULL,
	codiagfeatkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS coecoclass (
	ecoclasstypename TEXT (60) NOT NULL,
	ecoclassref TEXT (254),
	ecoclassid TEXT (30) NOT NULL,
	ecoclassname TEXT,
	cokey TEXT (30) NOT NULL,
	coecoclasskey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS coeplants (
	plantsym TEXT (8) NOT NULL,
	plantsciname TEXT (127),
	plantcomname TEXT (60),
	forestunprod INT16,
	rangeprod INT16,
	cokey TEXT (30) NOT NULL,
	coeplantskey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS coerosionacc (
	erokind TEXT (254),
	rvindicator TEXT (3) NOT NULL,
	cokey TEXT (30) NOT NULL,
	coeroacckey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS coforprod (
	plantsym TEXT (8) NOT NULL,
	plantsciname TEXT (127),
	plantcomname TEXT (60),
	siteindexbase TEXT (254),
	siteindex_l INT16,
	siteindex_r INT16,
	siteindex_h INT16,
	fprod_l FLOAT64,
	fprod_r FLOAT64,
	fprod_h FLOAT64,
	cokey TEXT (30) NOT NULL,
	cofprodkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS coforprodo (
	siteindexbase TEXT (254),
	siteindex_l INT16,
	siteindex_r INT16,
	siteindex_h INT16,
	fprod_l FLOAT64,
	fprod_r FLOAT64,
	fprod_h FLOAT64,
	fprodunits TEXT (254),
	cofprodkey TEXT (30) NOT NULL,
	cofprodokey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cofprodkey) REFERENCES coforprod(cofprodkey));""",

"""CREATE TABLE IF NOT EXISTS cogeomordesc (
	geomftname TEXT (30) NOT NULL,
	geomfname TEXT (50) NOT NULL,
	geomfmod TEXT (60),
	geomfeatid INT16,
	existsonfeat INT16,
	rvindicator TEXT (3) NOT NULL,
	cokey TEXT (30) NOT NULL,
	cogeomdkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cohydriccriteria (
	hydriccriterion TEXT (254),
	cokey TEXT (30) NOT NULL,
	cohydcritkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cointerp (
	cokey TEXT (30) NOT NULL,
	mrulekey TEXT (30) NOT NULL,
	mrulename TEXT (60) NOT NULL,
	seqnum INT16 NOT NULL,
	rulekey TEXT (30) NOT NULL,
	rulename TEXT (60) NOT NULL,
	ruledepth INT16 NOT NULL,
	interpll FLOAT64,
	interpllc TEXT (254),
	interplr FLOAT64,
	interplrc TEXT (254),
	interphr FLOAT64,
	interphrc TEXT (254),
	interphh FLOAT64,
	interphhc TEXT (254),
	nullpropdatabool TEXT (3),
	defpropdatabool TEXT (3),
	incpropdatabool TEXT (3),
	cointerpkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS comonth (
	monthseq INT16,
	month TEXT (254),
	flodfreqcl TEXT (254),
	floddurcl TEXT (254),
	pondfreqcl TEXT (254),
	ponddurcl TEXT (254),
	ponddep_l INT16,
	ponddep_r INT16,
	ponddep_h INT16,
	dlyavgprecip_l INT16,
	dlyavgprecip_r INT16,
	dlyavgprecip_h INT16,
	dlyavgpotet_l INT16,
	dlyavgpotet_r INT16,
	dlyavgpotet_h INT16,
	cokey TEXT (30) NOT NULL,
	comonthkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS component (
	comppct_l INT16,
	comppct_r INT16,
	comppct_h INT16,
	compname TEXT (60),
	compkind TEXT (254),
	majcompflag TEXT (3),
	otherph TEXT (40),
	localphase TEXT (40),
	slope_l FLOAT64,
	slope_r FLOAT64,
	slope_h FLOAT64,
	slopelenusle_l INT16,
	slopelenusle_r INT16,
	slopelenusle_h INT16,
	runoff TEXT (254),
	tfact INT16,
	wei TEXT (254),
	weg TEXT (254),
	erocl TEXT (254),
	earthcovkind1 TEXT (254),
	earthcovkind2 TEXT (254),
	hydricon TEXT (254),
	hydricrating TEXT (254),
	drainagecl TEXT (254),
	elev_l FLOAT64,
	elev_r FLOAT64,
	elev_h FLOAT64,
	aspectccwise INT16,
	aspectrep INT16,
	aspectcwise INT16,
	geomdesc TEXT,
	albedodry_l FLOAT64,
	albedodry_r FLOAT64,
	albedodry_h FLOAT64,
	airtempa_l FLOAT64,
	airtempa_r FLOAT64,
	airtempa_h FLOAT64,
	map_l INT16,
	map_r INT16,
	map_h INT16,
	reannualprecip_l INT16,
	reannualprecip_r INT16,
	reannualprecip_h INT16,
	ffd_l INT16,
	ffd_r INT16,
	ffd_h INT16,
	nirrcapcl TEXT (254),
	nirrcapscl TEXT (254),
	nirrcapunit INT16,
	irrcapcl TEXT (254),
	irrcapscl TEXT (254),
	irrcapunit INT16,
	cropprodindex INT16,
	constreeshrubgrp TEXT (254),
	wndbrksuitgrp TEXT (254),
	rsprod_l INTEGER,
	rsprod_r INTEGER,
	rsprod_h INTEGER,
	foragesuitgrpid TEXT (11),
	wlgrain TEXT (254),
	wlgrass TEXT (254),
	wlherbaceous TEXT (254),
	wlshrub TEXT (254),
	wlconiferous TEXT (254),
	wlhardwood TEXT (254),
	wlwetplant TEXT (254),
	wlshallowwat TEXT (254),
	wlrangeland TEXT (254),
	wlopenland TEXT (254),
	wlwoodland TEXT (254),
	wlwetland TEXT (254),
	soilslippot TEXT (254),
	frostact TEXT (254),
	initsub_l INT16,
	initsub_r INT16,
	initsub_h INT16,
	totalsub_l INT16,
	totalsub_r INT16,
	totalsub_h INT16,
	hydgrp TEXT (254),
	corcon TEXT (254),
	corsteel TEXT (254),
	taxclname TEXT (120),
	taxorder TEXT (254),
	taxsuborder TEXT (254),
	taxgrtgroup TEXT (254),
	taxsubgrp TEXT (254),
	taxpartsize TEXT (254),
	taxpartsizemod TEXT (254),
	taxceactcl TEXT (254),
	taxreaction TEXT (254),
	taxtempcl TEXT (254),
	taxmoistscl TEXT (254),
	taxtempregime TEXT (254),
	soiltaxedition TEXT (254),
	castorieindex INT16,
	flecolcomnum TEXT (5),
	flhe TEXT (3),
	flphe TEXT (3),
	flsoilleachpot TEXT (254),
	flsoirunoffpot TEXT (254),
	fltemik2use TEXT (3),
	fltriumph2use TEXT (3),
	indraingrp TEXT (3),
	innitrateleachi INT16,
	misoimgmtgrp TEXT (254),
	vasoimgtgrp TEXT (254),
	mukey TEXT (30) NOT NULL,
	cokey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(mukey) REFERENCES mapunit(mukey));""",

"""CREATE TABLE IF NOT EXISTS copm (
	pmorder INT16,
	pmmodifier TEXT (254),
	pmgenmod TEXT (60),
	pmkind TEXT (254),
	pmorigin TEXT (254),
	copmgrpkey TEXT (30) NOT NULL,
	copmkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(copmgrpkey) REFERENCES copmgrp(copmgrpkey));""",

"""CREATE TABLE IF NOT EXISTS copmgrp (
	pmgroupname TEXT (252),
	rvindicator TEXT (3) NOT NULL,
	cokey TEXT (30) NOT NULL,
	copmgrpkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS copwindbreak (
	wndbrkht_l FLOAT64,
	wndbrkht_r FLOAT64,
	wndbrkht_h FLOAT64,
	plantsym TEXT (8) NOT NULL,
	plantsciname TEXT (127),
	plantcomname TEXT (60),
	cokey TEXT (30) NOT NULL,
	copwindbreakkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS corestrictions (
	reskind TEXT (254),
	reshard TEXT (254),
	resdept_l INT16,
	resdept_r INT16,
	resdept_h INT16,
	resdepb_l INT16,
	resdepb_r INT16,
	resdepb_h INT16,
	resthk_l INT16,
	resthk_r INT16,
	resthk_h INT16,
	cokey TEXT (30) NOT NULL,
	corestrictkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cosoilmoist (
	soimoistdept_l INT16,
	soimoistdept_r INT16,
	soimoistdept_h INT16,
	soimoistdepb_l INT16,
	soimoistdepb_r INT16,
	soimoistdepb_h INT16,
	soimoiststat TEXT (254),
	comonthkey TEXT (30) NOT NULL,
	cosoilmoistkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(comonthkey) REFERENCES comonth(comonthkey));""",

"""CREATE TABLE IF NOT EXISTS cosoiltemp (
	soitempmm INT16,
	soitempdept_l INT16,
	soitempdept_r INT16,
	soitempdept_h INT16,
	soitempdepb_l INT16,
	soitempdepb_r INT16,
	soitempdepb_h INT16,
	comonthkey TEXT (30) NOT NULL,
	cosoiltempkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(comonthkey) REFERENCES comonth(comonthkey));""",

"""CREATE TABLE IF NOT EXISTS cosurffrags (
	sfragcov_l FLOAT64,
	sfragcov_r FLOAT64,
	sfragcov_h FLOAT64,
	distrocks_l FLOAT64,
	distrocks_r FLOAT64,
	distrocks_h FLOAT64,
	sfragkind TEXT (254),
	sfragsize_l INT16,
	sfragsize_r INT16,
	sfragsize_h INT16,
	sfragshp TEXT (254),
	sfraground TEXT (254),
	sfraghard TEXT (254),
	cokey TEXT (30) NOT NULL,
	cosurffragskey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cosurfmorphgc (
	geomposmntn TEXT (254),
	geomposhill TEXT (254),
	geompostrce TEXT (254),
	geomposflats TEXT (254),
	cogeomdkey TEXT (30) NOT NULL,
	cosurfmorgckey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cogeomdkey) REFERENCES cogeomordesc(cogeomdkey));""",

"""CREATE TABLE IF NOT EXISTS cosurfmorphhpp (
	hillslopeprof TEXT (254),
	cogeomdkey TEXT (30) NOT NULL,
	cosurfmorhppkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cogeomdkey) REFERENCES cogeomordesc(cogeomdkey));""",

"""CREATE TABLE IF NOT EXISTS cosurfmorphmr (
	geomicrorelief TEXT (254),
	cogeomdkey TEXT (30) NOT NULL,
	cosurfmormrkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cogeomdkey) REFERENCES cogeomordesc(cogeomdkey));""",

"""CREATE TABLE IF NOT EXISTS cosurfmorphss (
	shapeacross TEXT (254),
	shapedown TEXT (254),
	cogeomdkey TEXT (30) NOT NULL,
	cosurfmorsskey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cogeomdkey) REFERENCES cogeomordesc(cogeomdkey));""",

"""CREATE TABLE IF NOT EXISTS cotaxfmmin (
	taxminalogy TEXT (254),
	cokey TEXT (30) NOT NULL,
	cotaxfmminkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cotaxmoistcl (
	taxmoistcl TEXT (254),
	cokey TEXT (30) NOT NULL,
	cotaxmckey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cotext (
	recdate REALDATE,
	comptextkind TEXT (254),
	textcat TEXT (20),
	textsubcat TEXT (20),
	text TEXT,
	cokey TEXT (30) NOT NULL,
	cotextkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cotreestomng (
	plantsym TEXT (8) NOT NULL,
	plantsciname TEXT (127),
	plantcomname TEXT (60),
	cokey TEXT (30) NOT NULL,
	cotreestomngkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS cotxfmother (
	taxfamother TEXT (254),
	cokey TEXT (30) NOT NULL,
	cotaxfokey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(cokey) REFERENCES component(cokey));""",

"""CREATE TABLE IF NOT EXISTS distinterpmd (
	rulename TEXT (60),
	ruledesign TEXT (254) NOT NULL,
	ruledesc TEXT,
	dataafuse TEXT (3),
	mrecentrulecwlu REALDATE,
	rulekey TEXT (30) NOT NULL,
	distmdkey TEXT (30) NOT NULL,
	distinterpmdkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(distmdkey) REFERENCES distmd(distmdkey));""",

"""CREATE TABLE IF NOT EXISTS distlegendmd (
	areatypename TEXT (45),
	areasymbol TEXT (20),
	areaname TEXT (135),
	ssastatus TEXT (254),
	cordate REALDATE,
	exportcertstatus TEXT (254),
	exportcertdate REALDATE,
	exportmetadata TEXT,
	lkey TEXT (30) NOT NULL,
	distmdkey TEXT (30) NOT NULL,
	distlegendmdkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(distmdkey) REFERENCES distmd(distmdkey));""",

"""CREATE TABLE IF NOT EXISTS distmd (
	distgendate REALDATE,
	diststatus TEXT (254) NOT NULL,
	interpmaxreasons INT16,
	distmdkey TEXT (30) PRIMARY KEY);""",

"""CREATE TABLE IF NOT EXISTS featdesc (
	areasymbol TEXT (20) NOT NULL,
	spatialversion INTEGER NOT NULL,
	featsym TEXT (3) NOT NULL,
	featname TEXT (80) NOT NULL,
	featdesc TEXT NOT NULL,
	featkey TEXT (30) PRIMARY KEY);""",

"""CREATE TABLE IF NOT EXISTS featline (
	OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	areasymbol TEXT (20),
	spatialver FLOAT64,
	featsym TEXT (3),
	featkey TEXT (30));""",
						  
"""CREATE TABLE IF NOT EXISTS featpoint (
	OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	areasymbol TEXT (20),
	spatialver FLOAT64,
	featsym TEXT (3),
	featkey TEXT (30));""",

"""CREATE TABLE IF NOT EXISTS laoverlap (
	areatypename TEXT (45) NOT NULL,
	areasymbol TEXT (20) NOT NULL,
	areaname TEXT (135),
	areaovacres INTEGER,
	lkey TEXT (30) NOT NULL,
	lareaovkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(lkey) REFERENCES legend(lkey));""",

"""CREATE TABLE IF NOT EXISTS legend (
	areatypename TEXT (45) NOT NULL,
	areasymbol TEXT (20) NOT NULL,
	areaname TEXT (135),
	areaacres INTEGER,
	mlraoffice TEXT (254),
	legenddesc TEXT (60),
	ssastatus TEXT (254),
	mouagncyresp TEXT (254),
	projectscale INTEGER,
	cordate REALDATE,
	ssurgoarchived REALDATE,
	legendsuituse TEXT (254),
	legendcertstat TEXT (254),
	lkey TEXT (30) PRIMARY KEY);""",

"""CREATE TABLE IF NOT EXISTS legendtext (
	recdate REALDATE,
	legendtextkind TEXT (254),
	textcat TEXT (20),
	textsubcat TEXT (20),
	text TEXT,
	lkey TEXT (30) NOT NULL,
	legtextkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(lkey) REFERENCES legend(lkey));""",

"""CREATE TABLE IF NOT EXISTS mapunit (
	musym TEXT (6) NOT NULL,
	muname TEXT (175),
	mukind TEXT (254),
	mustatus TEXT (254),
	muacres INTEGER,
	mapunitlfw_l INT16,
	mapunitlfw_r INT16,
	mapunitlfw_h INT16,
	mapunitpfa_l FLOAT64,
	mapunitpfa_r FLOAT64,
	mapunitpfa_h FLOAT64,
	farmlndcl TEXT (254),
	muhelcl TEXT (254),
	muwathelcl TEXT (254),
	muwndhelcl TEXT (254),
	interpfocus TEXT (30),
	invesintens TEXT (254),
	iacornsr INT16,
	nhiforsoigrp TEXT (254),
	nhspiagr FLOAT64,
	vtsepticsyscl TEXT (254),
	mucertstat TEXT (254),
	lkey TEXT (30) NOT NULL,
	mukey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(lkey) REFERENCES legend(lkey));""",

"""CREATE TABLE IF NOT EXISTS mdstatdomdet (
	domainname TEXT (40) NOT NULL,
	choicesequence INT16 NOT NULL,
	choice TEXT (254) NOT NULL,
	choicedesc TEXT,
	choiceobsolete TEXT (3) NOT NULL,
	PRIMARY KEY (domainname, choicesequence));""",

"""CREATE TABLE IF NOT EXISTS mdstatdommas (
	domainname TEXT (40) PRIMARY KEY,
	domainmaxlen INT16 NOT NULL);""",

"""CREATE TABLE IF NOT EXISTS mdstatidxdet (
	tabphyname TEXT (30) NOT NULL,
	idxphyname TEXT (30) NOT NULL,
	idxcolsequence INT16 NOT NULL,
	colphyname TEXT (30) NOT NULL,
	PRIMARY KEY (tabphyname, idxphyname, idxcolsequence));""",

"""CREATE TABLE IF NOT EXISTS mdstatidxmas (
	tabphyname TEXT (30) NOT NULL,
	idxphyname TEXT (30) NOT NULL,
	uniqueindex TEXT (3) NOT NULL,
	PRIMARY KEY (tabphyname, idxphyname));""",

"""CREATE TABLE IF NOT EXISTS mdstatrshipdet (
	ltabphyname TEXT (30) NOT NULL,
	rtabphyname TEXT (30) NOT NULL,
	relationshipname TEXT (30) NOT NULL,
	ltabcolphyname TEXT (30) NOT NULL,
	rtabcolphyname TEXT (30) NOT NULL,
	PRIMARY KEY (ltabphyname, rtabphyname, relationshipname, ltabcolphyname, rtabcolphyname));""",

"""CREATE TABLE IF NOT EXISTS mdstatrshipmas (
	ltabphyname TEXT (30) NOT NULL,
	rtabphyname TEXT (30) NOT NULL,
	relationshipname TEXT (30) NOT NULL,
	cardinality TEXT (254) NOT NULL,
	mandatory TEXT (3) NOT NULL,
	PRIMARY KEY (ltabphyname, rtabphyname, relationshipname));""",

"""CREATE TABLE IF NOT EXISTS mdstattabcols (
	tabphyname TEXT (30) NOT NULL,
	colsequence INT16 NOT NULL,
	colphyname TEXT (30) NOT NULL,
	collogname TEXT (30) NOT NULL,
	collabel TEXT (80) NOT NULL,
	logicaldatatype TEXT (254) NOT NULL,
	not_null TEXT (3) NOT NULL,  --changed notnull -> not_null
	fieldsize INT16,
	precision INT16,
	minimum FLOAT64,
	maximum FLOAT64,
	uom TEXT (60),
	domainname TEXT (40),
	coldesc TEXT NOT NULL,
	PRIMARY KEY (tabphyname, colsequence));""",

"""CREATE TABLE IF NOT EXISTS mdstattabs (
	tabphyname TEXT (30) PRIMARY KEY,
	tablogname TEXT (30) NOT NULL,
	tablabel TEXT (80) NOT NULL,
	tabdesc TEXT NOT NULL,
	iefilename TEXT (30) NOT NULL);""",

"""CREATE TABLE IF NOT EXISTS month (
	monthseq INT16 NOT NULL,
	monthname TEXT (9) PRIMARY KEY);""",

"""CREATE TABLE IF NOT EXISTS muaggatt (
	musym TEXT (6) NOT NULL,
	muname TEXT (175),
	mustatus TEXT (254),
	slopegraddcp FLOAT64,
	slopegradwta FLOAT64,
	brockdepmin INT16,
	wtdepannmin INT16,
	wtdepaprjunmin INT16,
	flodfreqdcd TEXT (254),
	flodfreqmax TEXT (254),
	pondfreqprs TEXT (254),
	aws025wta FLOAT64,
	aws050wta FLOAT64,
	aws0100wta FLOAT64,
	aws0150wta FLOAT64,
	drclassdcd TEXT (254),
	drclasswettest TEXT (254),
	hydgrpdcd TEXT (254),
	iccdcd TEXT (254),
	iccdcdpct INT16,
	niccdcd TEXT (254),
	niccdcdpct INT16,
	engdwobdcd TEXT (254),
	engdwbdcd TEXT (254),
	engdwbll TEXT (254),
	engdwbml TEXT (254),
	engstafdcd TEXT (254),
	engstafll TEXT (254),
	engstafml TEXT (254),
	engsldcd TEXT (254),
	engsldcp TEXT (254),
	englrsdcd TEXT (254),
	engcmssdcd TEXT (254),
	engcmssmp TEXT (254),
	urbrecptdcd TEXT (254),
	urbrecptwta FLOAT64,
	forpehrtdcp TEXT (254),
	hydclprs TEXT (254),
	awmmfpwwta FLOAT64,
	mukey TEXT (30) PRIMARY KEY);""",

"""CREATE TABLE IF NOT EXISTS muaoverlap (
	areaovacres INTEGER,
	lareaovkey TEXT (30) NOT NULL,
	mukey TEXT (30) NOT NULL,
	muareaovkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(mukey) REFERENCES mapunit(mukey));""",

"""CREATE TABLE IF NOT EXISTS mucropyld (
	cropname TEXT (254),
	yldunits TEXT (254),
	nonirryield_l FLOAT64,
	nonirryield_r FLOAT64,
	nonirryield_h FLOAT64,
	irryield_l FLOAT64,
	irryield_r FLOAT64,
	irryield_h FLOAT64,
	mukey TEXT (30) NOT NULL,
	mucrpyldkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(mukey) REFERENCES mapunit(mukey));""",

"""CREATE TABLE IF NOT EXISTS muline (
	OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	areasymbol TEXT (20),
	spatialver FLOAT64,
	musym TEXT (6),
	mukey TEXT (30));""",

							  
"""CREATE TABLE IF NOT EXISTS mupoint (
	OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	areasymbol TEXT (20),
	spatialver FLOAT64,
	musym TEXT (6),
	mukey TEXT (30));""",

							  
"""CREATE TABLE IF NOT EXISTS mupolygon (
	OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	areasymbol TEXT (20),
	spatialver FLOAT64,
	musym TEXT (6),
	mukey TEXT (30));""",

"""CREATE TABLE IF NOT EXISTS mutext (
	recdate REALDATE,
	mapunittextkind TEXT (254),
	textcat TEXT (20),
	textsubcat TEXT (20),
	text TEXT,
	mukey TEXT (30) NOT NULL,
	mutextkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(mukey) REFERENCES mapunit(mukey));""",

"""CREATE TABLE IF NOT EXISTS sacatalog (
	areasymbol TEXT (20) NOT NULL,
	areaname TEXT (135) NOT NULL,
	saversion INTEGER NOT NULL,
	saverest REALDATE NOT NULL,
	tabularversion INTEGER NOT NULL,
	tabularverest REALDATE NOT NULL,
	tabnasisexportdate REALDATE NOT NULL,
	tabcertstatus TEXT (254),
	tabcertstatusdesc TEXT,
	fgdcmetadata TEXT NOT NULL,
	sacatalogkey TEXT (30) PRIMARY KEY);""",

"""CREATE TABLE IF NOT EXISTS sainterp (
	areasymbol TEXT (20) NOT NULL,
	interpname TEXT (60) NOT NULL,
	interptype TEXT (254) NOT NULL,
	interpdesc TEXT,
	interpdesigndate REALDATE NOT NULL,
	interpgendate REALDATE NOT NULL,
	interpmaxreasons INT16,
	sacatalogkey TEXT (30) NOT NULL,
	sainterpkey TEXT (30) PRIMARY KEY,
	FOREIGN KEY(sacatalogkey) REFERENCES sacatalog(sacatalogkey));""",

	
"""CREATE TABLE IF NOT EXISTS sapolygon (
	OBJECTID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	areasymbol TEXT (20),
	spatialver FLOAT64,
	lkey TEXT (30));""",

"""CREATE TABLE IF NOT EXISTS sdvalgorithm (
	algorithmsequence INT16 NOT NULL,
	algorithmname TEXT (50) PRIMARY KEY,
	algorithminitials TEXT (3) NOT NULL,
	algorithmdescription TEXT NOT NULL);""",

"""CREATE TABLE IF NOT EXISTS sdvattribute (
	attributekey INTEGER PRIMARY KEY,
	attributename TEXT (60) NOT NULL,
	attributetablename TEXT (30) NOT NULL,
	attributecolumnname TEXT (30) NOT NULL,
	attributelogicaldatatype TEXT (20) NOT NULL,
	attributefieldsize INT16,
	attributeprecision INT16,
	attributedescription TEXT NOT NULL,
	attributeuom TEXT (60),
	attributeuomabbrev TEXT (30),
	attributetype TEXT (20) NOT NULL,
	nasisrulename TEXT (60),
	ruledesign INT16,
	notratedphrase TEXT (254),
	mapunitlevelattribflag INT16 NOT NULL,
	complevelattribflag INT16 NOT NULL,
	cmonthlevelattribflag INT16 NOT NULL,
	horzlevelattribflag INT16 NOT NULL,
	tiebreakdomainname TEXT (40),
	tiebreakruleoptionflag INT16 NOT NULL,
	tiebreaklowlabel TEXT (20),
	tiebreakhighlabel TEXT (20),
	tiebreakrule INT16 NOT NULL,
	resultcolumnname TEXT (10) NOT NULL,
	sqlwhereclause TEXT (255),
	primaryconcolname TEXT (30),
	pcclogicaldatatype TEXT (20),
	primaryconstraintlabel TEXT (30),
	secondaryconcolname TEXT (30),
	scclogicaldatatype TEXT (20),
	secondaryconstraintlabel TEXT (30),
	dqmodeoptionflag INT16 NOT NULL,
	depthqualifiermode TEXT (20),
	layerdepthtotop FLOAT64,
	layerdepthtobottom FLOAT64,
	layerdepthuom TEXT (20),
	monthrangeoptionflag INT16 NOT NULL,
	beginningmonth TEXT (9),
	endingmonth TEXT (9),
	horzaggmeth TEXT (30),
	interpnullsaszerooptionflag INT16 NOT NULL,
	interpnullsaszeroflag INT16 NOT NULL,
	nullratingreplacementvalue TEXT (254),
	basicmodeflag INT16 NOT NULL,
	maplegendkey INTEGER NOT NULL,
	maplegendclasses INT16,
	maplegendxml TEXT NOT NULL,
	nasissiteid INTEGER NOT NULL,
	wlupdated REALDATE NOT NULL,
	algorithmname TEXT (50) NOT NULL,
	componentpercentcutoff INT16,
	readytodistribute INT16 NOT NULL,
	effectivelogicaldatatype TEXT (20) NOT NULL);""",

"""CREATE TABLE IF NOT EXISTS sdvfolder (
	foldersequence INT16 NOT NULL,
	foldername TEXT (80) NOT NULL,
	folderdescription TEXT NOT NULL,
	folderkey INTEGER PRIMARY KEY,
	parentfolderkey INTEGER,
	wlupdated REALDATE NOT NULL);""",

"""CREATE TABLE IF NOT EXISTS sdvfolderattribute (
	folderkey INTEGER NOT NULL,
	attributekey INTEGER NOT NULL,
	PRIMARY KEY (folderkey, attributekey));""",

"""CREATE TABLE IF NOT EXISTS version (
	areasymbol TEXT (20),
	datatype TEXT (20),
	version TEXT (20),
	PRIMARY KEY (areasymbol, datatype));""",

"""SELECT AddGeometryColumn('featline', 'SHAPE', 4326, 'MULTILINESTRING', 'XY');""",
"""SELECT AddGeometryColumn('featpoint', 'SHAPE', 4326, 'MULTIPOINT', 'XY');""",
"""SELECT AddGeometryColumn('muline', 'SHAPE', 4326, 'MULTILINESTRING', 'XY');""",
"""SELECT AddGeometryColumn('mupoint', 'SHAPE', 4326, 'MULTIPOINT', 'XY');""",
"""SELECT AddGeometryColumn('mupolygon', 'SHAPE', 4326, 'MULTIPOLYGON', 'XY');""",
"""SELECT AddGeometryColumn('sapolygon', 'SHAPE', 4326, 'MULTIPOLYGON', 'XY');"""
]
