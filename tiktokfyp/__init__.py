from .tiktokfyp import TikTokFYP

async def setup(bot):
   await bot.add_cog(TikTokFYP(bot))
