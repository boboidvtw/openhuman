import zhTW1 from './chunks/zh-TW-1';
import zhTW2 from './chunks/zh-TW-2';
import zhTW3 from './chunks/zh-TW-3';
import zhTW4 from './chunks/zh-TW-4';
import zhTW5 from './chunks/zh-TW-5';
import type { TranslationMap } from './types';

// Simplified Chinese (简体中文) translations. Each chunk maps to chunks/en-N.ts.
// Missing keys fall back to English via I18nContext.resolveEn().
const zhTW: TranslationMap = { ...zhTW1, ...zhTW2, ...zhTW3, ...zhTW4, ...zhTW5 };

export default zhTW;
