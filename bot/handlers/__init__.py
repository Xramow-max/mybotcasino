# - *- coding: utf- 8 - *-

## START COMMAND    
from bot.handlers.start_msg import dp 

from bot.handlers.channel_game.mail_channel_game import dp 


## ADMIN HANDLER.
from bot.handlers.admin.kazna.start_kazna_call import dp 
from bot.handlers.admin.statistic.start_statistic import dp 

## PROFILE HANDLER.
from bot.handlers.user.profile.profile import dp 
from bot.handlers.user.profile.referal_program.referal_program import dp
from bot.handlers.user.profile.change_balance.add_balance import dp 
from bot.handlers.user.profile.change_balance.dell_balance import dp 

## GAME BOT HANDLER
from bot.handlers.user.game_bot.start_game_bot import dp
from bot.handlers.user.game_bot.knb_game.start_knb_game import dp 
from bot.handlers.user.game_bot.slot_game.slot_game import dp 

## INFO HANDLER.
from bot.handlers.user.info.start_info import dp 


__all__ = ['dp']