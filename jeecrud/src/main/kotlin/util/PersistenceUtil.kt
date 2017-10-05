package util

import javax.persistence.EntityManager
import javax.persistence.EntityManagerFactory
import javax.persistence.Persistence

object PersistenceUtil {
    private var entityManagerFactory: EntityManagerFactory = Persistence.createEntityManagerFactory("jeecrud")

    fun getEntityManager(): EntityManager {
        return entityManagerFactory.createEntityManager()
    }
}