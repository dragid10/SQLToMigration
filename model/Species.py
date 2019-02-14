class Species:
    def __init__(self, oid, user_id, version, species_name, common_name, family, miami_name,
                 food, medicinal, material, customsl, technology, alt_word_form, french_name,
                 literal_meaning, beech_maple_forest, oak_forest, beech_oak_maple, oak_savanna, dry_prairie,
                 wet_prairie, lowland_deciduous, conifer_shrubland_and_forest, conifer_swamp, deciduous_swamp, wetland,
                 geboe_property, liebert_property, grant_property, seven_pillars, agricultural_areas,
                 human_disturbed_areas, tree, shrub, herb, vine, unkn, winter, summer, fall, spring, related_words,
                 na, cultivated, wild, earliest_record, latest_record, created_at, updated_at):
        self.oid = oid
        self.user_id = user_id
        self.version = version
        self.species_name = species_name
        self.common_name = common_name
        self.family = family
        self.miami_name = miami_name
        self.food = food
        self.medicinal = medicinal
        self.material = material
        self.customsl = customsl
        self.technology = technology
        self.alt_word_form = alt_word_form
        self.french_name = french_name
        self.literal_meaning = literal_meaning
        self.beech_maple_forest = beech_maple_forest
        self.oak_forest = oak_forest
        self.beech_oak_maple = beech_oak_maple
        self.oak_savanna = oak_savanna
        self.dry_prairie = dry_prairie
        self.wet_prairie = wet_prairie
        self.lowland_deciduous = lowland_deciduous
        self.conifer_shrubland_and_forest = conifer_shrubland_and_forest
        self.conifer_swamp = conifer_swamp
        self.deciduous_swamp = deciduous_swamp
        self.wetland = wetland
        self.geboe_property = geboe_property
        self.liebert_property = liebert_property
        self.grant_property = grant_property
        self.seven_pillars = seven_pillars
        self.agricultural_areas = agricultural_areas
        self.human_disturbed_areas = human_disturbed_areas
        self.tree = tree
        self.shrub = shrub
        self.herb = herb
        self.vine = vine
        self.unkn = unkn
        self.winter = winter
        self.summer = summer
        self.fall = fall
        self.spring = spring
        self.related_words = related_words
        self.na = na
        self.cultivated = cultivated
        self.wild = wild
        self.earliest_record = earliest_record
        self.latest_record = latest_record
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return """
        'oid' => '{oid}', 
        'user_id' => '{user_id}', 
        'version' => '{version}', 
        'species_name' => '{species_name}', 
        'common_name' => '{common_name}', 
        'family' => '{family}', 
        'miami_name' => '{miami_name}', 
        'food' => '{food}', 
        'medicinal' => '{medicinal}', 
        'material' => '{material}', 
        'customsl' => '{customsl}', 
        'technology' => '{technology}', 
        'alt_word_form' => '{alt_word_form}', 
        'french_name' => '{french_name}', 
        'literal_meaning' => '{literal_meaning}', 
        'beech_maple_forest' => '{beech_maple_forest}', 
        'oak_forest' => '{oak_forest}', 
        'beech_oak_maple' => '{beech_oak_maple}', 
        'oak_savanna' => '{oak_savanna}', 
        'dry_prairie' => '{dry_prairie}', 
        'wet_prairie' => '{wet_prairie}', 
        'lowland_deciduous' => '{lowland_deciduous}', 
        'conifer_shrubland_and_forest' => '{conifer_shrubland_and_forest}', 
        'conifer_swamp' => '{conifer_swamp}', 
        'deciduous_swamp' => '{deciduous_swamp}', 
        'wetland' => '{wetland}', 
        'geboe_property' => '{geboe_property}', 
        'liebert_property' => '{liebert_property}', 
        'grant_property' => '{grant_property}', 
        'seven_pillars' => '{seven_pillars}', 
        'agricultural_areas' => '{agricultural_areas}', 
        'human_disturbed_areas' => '{human_disturbed_areas}', 
        'tree' => '{tree}', 
        'shrub' => '{shrub}', 
        'herb' => '{herb}', 
        'vine' => '{vine}', 
        'unkn' => '{unkn}', 
        'winter' => '{winter}', 
        'summer' => '{summer}', 
        'fall' => '{fall}', 
        'spring' => '{spring}', 
        'related_words' => '{related_words}', 
        'na' => '{na}', 
        'cultivated' => '{cultivated}', 
        'wild' => '{wild}', 
        'earliest_record' => '{earliest_record}', 
        'latest_record' => '{latest_record}', 
        'created_at' => '{created_at}', 
        'updated_at' => '{updated_at}'   
                """.format(oid=self.oid, user_id=self.user_id, version=self.version,
                           species_name=self.species_name, common_name=self.common_name, family=self.family,
                           miami_name=self.miami_name,
                           food=self.food, medicinal=self.medicinal,
                           material=self.material, customsl=self.customsl, technology=self.technology,
                           alt_word_form=self.alt_word_form,
                           french_name=self.french_name,
                           literal_meaning=self.literal_meaning,
                           beech_maple_forest=self.beech_maple_forest, oak_forest=self.oak_forest,
                           beech_oak_maple=self.beech_oak_maple, oak_savanna=self.oak_savanna,
                           dry_prairie=self.dry_prairie, wet_prairie=self.wet_prairie,
                           lowland_deciduous=self.lowland_deciduous,
                           conifer_shrubland_and_forest=self.conifer_shrubland_and_forest,
                           conifer_swamp=self.conifer_swamp, deciduous_swamp=self.deciduous_swamp, wetland=self.wetland,
                           geboe_property=self.geboe_property, liebert_property=self.liebert_property,
                           grant_property=self.grant_property, seven_pillars=self.seven_pillars,
                           agricultural_areas=self.agricultural_areas,
                           human_disturbed_areas=self.human_disturbed_areas, tree=self.tree, shrub=self.shrub,
                           herb=self.herb, vine=self.vine, unkn=self.unkn, winter=self.winter, summer=self.summer,
                           fall=self.fall, spring=self.spring, related_words=self.related_words,
                           na=self.na,
                           cultivated=self.cultivated, wild=self.wild, earliest_record=self.earliest_record,
                           latest_record=self.latest_record,
                           created_at=self.created_at, updated_at=self.updated_at).rstrip().lstrip()
