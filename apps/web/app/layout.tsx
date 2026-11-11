import type {Metadata} from "next";
import "./globals.css";
export const metadata:Metadata={title:"VideoCreate — AI Motion Studio",description:"Turn a creative brief into a motion-designed video."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="ru"><body>{children}</body></html>}
