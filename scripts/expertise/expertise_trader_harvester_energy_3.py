import sys

def addExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'trader_1a':
		return

	actor.addSkill('expertise_trader_harvester_energy_3')

	actor.addSkillMod('expertise_harvester_energy_decrease', 5)

	addAbilities(core, actor, player)

	return

def removeExpertisePoint(core, actor):

	player = actor.getSlottedObject('ghost')

	if not player:
		return

	if not player.getProfession() == 'trader_1a':
		return

	actor.removeSkill('expertise_trader_harvester_energy_3')

	actor.removeSkillMod('expertise_harvester_energy_decrease', 5)

	removeAbilities(core, actor, player)

	return

# this checks what abilities the player gets by level, need to also call this on level-up
def addAbilities(core, actor, player):


	return

def removeAbilities(core, actor, player):


	return