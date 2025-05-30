import instaloader
import re

def fetch_instagram_data(username):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        return {
            "username": profile.username,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "verified": profile.is_verified,
            "profile_pic_url": profile.profile_pic_url
        }
    except Exception as e:
        print(f"[Error] Failed to fetch data for {username}: {e}")
        return None

def analyze_profile(profile_url):
    print(f"[Analyzer] Analyzing profile: {profile_url}")

    if "instagram.com" not in profile_url:
        return {
            "platform": "Unknown",
            "username": "unknown_user",
            "bio": "Could not extract bio.",
            "trust_score": 25,
            "red_flags": ["Unsupported platform", "No data retrieved"],
            "verified": False,
            "profile_pic_url": ""
        }

    username = profile_url.rstrip("/").split("/")[-1]
    data = fetch_instagram_data(username)

    if not data:
        return {
            "platform": "Instagram",
            "username": username,
            "bio": "Could not fetch data.",
            "trust_score": 20,
            "red_flags": ["Profile not found or private"],
            "verified": False,
            "profile_pic_url": ""
        }

    bio = data["bio"]
    followers = data["followers"]
    verified = data["verified"]
    profile_pic_url = data["profile_pic_url"]

    red_flags = []
    positive_factors = []

    trust_score = 50

    if verified:
        trust_score += 30
        positive_factors.append("Account is verified")
    else:
        red_flags.append("Account is not verified")

    if followers > 1000000:
        trust_score += 15
        positive_factors.append("Very high follower count")
    elif followers > 10000:
        trust_score += 10
        positive_factors.append("High follower count")
    elif followers < 300:
        trust_score -= 15
        red_flags.append("Very low follower count")

    if len(bio.strip()) < 10:
        trust_score -= 10
        red_flags.append("Bio too short or generic")
    elif "fan" in bio.lower() or "parody" in bio.lower():
        trust_score -= 10
        red_flags.append("Bio suggests it's a fan or parody account")
    else:
        positive_factors.append("Bio looks authentic")

    trust_score = max(0, min(100, trust_score))  

    return {
        "platform": "Instagram",
        "username": data["username"],
        "bio": bio,
        "followers": followers,
        "following": data["following"],
        "verified": verified,
        "profile_pic_url": str(profile_pic_url),
        "trust_score": trust_score,
        "red_flags": red_flags,
        "positive_factors": positive_factors
    }
