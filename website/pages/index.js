import Head from 'next/head';
import styles from '../styles/Home.module.css';

import Link from 'next/link'
import { useRouter } from 'next/router'


export default function Home() {
  const router = useRouter()
  return (
    <div className={styles.container}>
      <Head>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header>
        <ul>
          <li>
            <Link href="/">Home</Link>
          </li>
          <li>
            <Link href="/about">About Us</Link>
          </li>
          <li>
            <Link href="/substitution">Sensory Substitution</Link>
          </li>
        </ul>
      </header>
      <main>
       Home
      </main>

      <footer>

      </footer>
    </div>
  )
}
