package util

import javax.persistence.EntityManager
import javax.persistence.EntityManagerFactory
import javax.persistence.Persistence


/**
 * @author Markus Reichl
 * @version 05.10.2017
 *
 * Utility class providing a getter for the EntityManager
 */
object PersistenceUtil {
    private var entityManagerFactory: EntityManagerFactory = Persistence.createEntityManagerFactory("jeecrud")

    /**
     * @return EntityManager instance
     */
    fun getEntityManager(): EntityManager {
        return entityManagerFactory.createEntityManager()
    }
}