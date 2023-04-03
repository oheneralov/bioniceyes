import Head from 'next/head'
import SimpleLayout from '../components/layout/simple'
import ArticlesJumbo from '../components/general/articles'

export default function Home(initialData) {
  console.log('initialData ', initialData)
  return (
    <SimpleLayout preContainer={<ArticlesJumbo menu="Home" />}>
      <div className="row">
        <p>
          {initialData.data.content.Home}
        </p>
      </div>
    </SimpleLayout>
  )
}

// This gets called on every request
export async function getServerSideProps(context) {
  const host = context.req.headers.host
  // Fetch data from external API
  const res = await fetch(`http://${host}/data.json`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}

