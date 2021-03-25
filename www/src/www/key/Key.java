package www.key;

import java.util.HashMap;
import java.util.Map;

public class Key {

	private Map<Kyes, String> keys = new HashMap();
	public static enum Kyes {
			NAVER_SEARCH_ID,
			NAVER_SEARCH_SECRET,
			NAVER_CAPCHA_ID,
			NAVER_CAPCHA_SECRET,
			DATA_COVID19_SERVICEKEY,
			JUSO,
			KAKAO_MAP_APPKEY
	}

	{
		keys.put(Kyes.NAVER_SEARCH_ID, "BQ1uoKa6ERSfHgNoDpx7");
		keys.put(Kyes.NAVER_SEARCH_SECRET, "vu9DMk8ZJq");
		keys.put(Kyes.NAVER_CAPCHA_ID, "pFgx5bVi0jbV8IhlRIqk");
		keys.put(Kyes.NAVER_CAPCHA_SECRET, "fviWLwyZrV");
		keys.put(Kyes.DATA_COVID19_SERVICEKEY, "Jq4YWKroCGb7FcfALTbqDwjFQMYdwUfkjkCE6NytaMQhm3i79IgAqLwWXtP794k6OqcvtprRBUHs5vo0YaNHZQ%3D%3D");
		keys.put(Kyes.JUSO, "devU01TX0FVVEgyMDIwMTIzMTEwMDkyNTExMDYxMjI=");
		keys.put(Kyes.KAKAO_MAP_APPKEY, "6149ea934d2b9a86f22e4c11df7797b0");
	}

	public Map<Kyes, String> getKeys() {
		return keys;
	}

}